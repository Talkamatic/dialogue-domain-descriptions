from sets import Set
from tdm.tdmlib import DeviceWHQuery, DeviceAction, EntityRecognizer
from incremental_search.contacts import CONTACTS

class IncrementalSearchDevice:
    class Call(DeviceAction):
        PARAMETERS = ["selected_contact", "selected_first_name=''", "selected_last_name=''"]
        def perform(self, selected_contact, first_name, last_name):
            if selected_contact not in CONTACTS:
                available_contacts = self.device.available_contacts(first_name, last_name)
                assert len(available_contacts) == 1
                selected_contact = available_contacts.pop()
            contact = CONTACTS[selected_contact]
            number = contact["number"]
            full_name = "%s %s" % (contact["first_name"], contact["last_name"])
            print "Calling %s at %s" % (full_name, number)
            return True

    class selected_contact(DeviceWHQuery):
        PARAMETERS = ["selected_first_name=''", "selected_last_name=''"]
        def perform(self, first_name, last_name):
            available_contacts = self.device.available_contacts(first_name, last_name)
            result = result = []
            for contact_id in available_contacts:
                contact = CONTACTS[contact_id]
                full_name = "%s %s" % (contact["first_name"], contact["last_name"])
                result.append({"name": contact_id, "sort": "contact", "grammar_entry": full_name})
            return result

    class ContactNameRecognizer(EntityRecognizer):
        def recognize_entity(self, string):
            result = []
            words = string.lower().split()
            for contact_id, contact in CONTACTS.iteritems():
                first_name = contact["first_name"]
                last_name = contact["last_name"]
                if first_name.lower() in words:
                    result.append({"name": first_name, "sort": "first_name", "grammar_entry": first_name.lower()})
                if last_name.lower() in words:
                    result.append({"name": last_name, "sort": "last_name", "grammar_entry": last_name.lower()})
            return result

    @classmethod
    def available_contacts(cls, first_name, last_name):
        matching_first_name_contacts = cls.contacts_with_matching_first_name(first_name)
        matching_last_name_contacts = cls.contacts_with_matching_last_name(last_name)
        available_contacts = matching_first_name_contacts.intersection(matching_last_name_contacts)
        return available_contacts

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
