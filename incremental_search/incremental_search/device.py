from sets import Set

from tdm.lib.device import DeviceWHQuery, DeviceAction, EntityRecognizer, DddDevice

from incremental_search.contacts import CONTACTS, FIRST_NAMES, LAST_NAMES, PHONE_NUMBERS


class IncrementalSearchDevice(DddDevice):
    language = "eng"

    class Call(DeviceAction):
        PARAMETERS = ["selected_contact"]
        def perform(self, selected_contact):
            number = self.device.number_of(selected_contact)
            # TODO: Implement calling
            success = True
            return success

    class selected_contact(DeviceWHQuery):
        PARAMETERS = ["selected_first_name=''", "selected_last_name=''"]
        def perform(self, first_name, last_name):
            available_contacts = self.device.available_contacts(first_name, last_name)
            result = []
            for contact_id in available_contacts:
                full_name = self.device.full_name_of(contact_id)
                result.append({"name": contact_id, "sort": "contact", "grammar_entry": full_name})
            return result

    class ContactNameRecognizer(EntityRecognizer):
        def recognize(self, string, language):
            self.device.__class__.language = language
            result = []
            words = string.lower().split()
            first_names = self._entities_of_first_names(words, language)
            result.extend(first_names)
            last_names = self._entities_of_last_names(words, language)
            result.extend(last_names)
            return result

        def _entities_of_first_names(self, words, language):
            first_names = FIRST_NAMES[language]
            return self._entities_of_names(words, first_names, "first_name")

        def _entities_of_last_names(self, words, language):
            last_names = LAST_NAMES[language]
            return self._entities_of_names(words, last_names, "last_name")

        def _entities_of_names(self, words, names, sort):
            results = []
            for name, identifier in names.iteritems():
                if name.lower() in words:
                    results.append({"name": identifier, "sort": sort, "grammar_entry": name.lower()})
            return results

    @classmethod
    def number_of(cls, contact_id):
        number = PHONE_NUMBERS[contact_id]
        return number

    @classmethod
    def full_name_of(cls, contact_id):
        first_name = cls.first_name_of_contact(contact_id)
        last_name = cls.last_name_of_contact(contact_id)
        full_name = "%s %s" % (first_name, last_name)
        return full_name

    @classmethod
    def first_name_of_contact(cls, contact):
        identifier = CONTACTS[contact]["first_name"]
        return cls.name_of_identifier(FIRST_NAMES[cls.language], identifier)

    @classmethod
    def last_name_of_contact(cls, contact):
        identifier = CONTACTS[contact]["last_name"]
        return cls.name_of_identifier(LAST_NAMES[cls.language], identifier)

    @classmethod
    def name_of_identifier(cls, names, identifier):
        matching_names = [name for name, actual_id in names.iteritems() if actual_id == identifier]
        assert len(matching_names) == 1, "Expected to find one matching name but found %s for %s among %s" %\
                                         (matching_names, identifier, names)
        return matching_names.pop()

    @classmethod
    def available_contacts(cls, first_name, last_name):
        matching_first_name_contacts = cls.contacts_with_matching_first_name(first_name)
        matching_last_name_contacts = cls.contacts_with_matching_last_name(last_name)
        available_contacts = matching_first_name_contacts.intersection(matching_last_name_contacts)
        return available_contacts

    @classmethod
    def first_available_contact(cls, first_name, last_name):
        available_contacts = cls.available_contacts(first_name, last_name)
        assert len(available_contacts) == 1
        selected_contact = available_contacts.pop()
        return selected_contact

    @classmethod
    def contacts_with_matching_first_name(cls, first_name):
        return cls.contacts_with_matching("first_name", first_name)

    @classmethod
    def contacts_with_matching_last_name(cls, last_name):
        return cls.contacts_with_matching("last_name", last_name)

    @classmethod
    def contacts_with_matching(cls, key, value):
        if not value:
            return Set(CONTACTS.keys())
        return Set([contact_id for contact_id, contact in CONTACTS.iteritems() if contact[key].lower() == value.lower()])
