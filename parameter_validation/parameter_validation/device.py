# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction, Validity, DddDevice


class ParameterValidationDevice(DddDevice):
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
    class Call(DeviceAction):
        def perform(self, selected_contact):
            number = self.device.PHONE_NUMBERS.get(selected_contact)
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

    class PhoneNumberAvailable(Validity):
        def is_valid(self, selected_contact):
            number = self.device.PHONE_NUMBERS.get(selected_contact)
            if number:
                return True
            return False
