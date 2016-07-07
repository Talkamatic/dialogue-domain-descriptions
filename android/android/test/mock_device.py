# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction, Validity, DeviceWHQuery, DddDevice


class AndroidDevice(DddDevice):
    JOHN = "contact_john"
    LISA = "contact_lisa"
    MARY = "contact_mary"
    ANDY = "contact_andy"

    PHONE_NUMBERS = {
        JOHN: "0701234567",
        LISA: "0709876543",
        MARY: "0706574839",
        ANDY: None,
    }

    CONTACTS_ENGLISH = {
        "John": JOHN,
        "Lisa": LISA,
        "Mary": MARY,
        "Andy": ANDY,
    }

    CONTACTS_FRENCH = {
        "Jean": JOHN,
        u"Élise": LISA,
        "Marie": MARY,
        u"André": ANDY,
    }

    CONTACTS_DUTCH = {
        "Jan": JOHN,
        "Lisa": LISA,
        "Maria": MARY,
        "Andreas": ANDY,
    }

    CONTACTS = {
        "eng": CONTACTS_ENGLISH,
        "fre": CONTACTS_FRENCH,
        "dut": CONTACTS_DUTCH,
    }

    def is_number_valid(self, number):
        if number:
            return True
        return False

    class Call(DeviceAction):
        PARAMETERS = ["selected_contact_to_call.grammar_entry"]
        def perform(self, selected_contact_to_call):
            number = self.device.PHONE_NUMBERS.get(selected_contact_to_call)
            # TODO: Implement calling
            success = True
            return success

    class ContactRecognizer(EntityRecognizer):
        def recognize(self, string, language):
            result = []
            words = string.lower().split()
            contacts = self.device.CONTACTS[language]
            for contact_name, identifier in contacts.iteritems():
                if contact_name.lower() in words:
                    recognized_entity = {
                        "sort": "contact",
                        "grammar_entry": contact_name,
                        "name": identifier,
                    }
                    result.append(recognized_entity)
            return result
            
    class CallerNumberAvailable(Validity):
        PARAMETERS = ["selected_contact_to_call"]
        def is_valid(self, contact):
            number = self.device.PHONE_NUMBERS.get(contact)
            return self.device.is_number_valid(number)

    class PhoneNumberAvailable(Validity):
        PARAMETERS = ["selected_contact_of_phone_number"]
        def is_valid(self, contact):
            number = self.device.PHONE_NUMBERS.get(contact)
            return self.device.is_number_valid(number)

    class phone_number_of_contact(DeviceWHQuery):
        PARAMETERS = ["selected_contact_of_phone_number"]
        def perform(self, selected_contact_of_phone_number):
            number = self.device.PHONE_NUMBERS.get(selected_contact_of_phone_number)
            if not self.device.is_number_valid(number):
                return []

            number_entity = {
                "grammar_entry": number
            }
            return [number_entity]
