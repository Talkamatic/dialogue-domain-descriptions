from tdm.lib.device import EntityRecognizer, DeviceAction, Validity, DeviceWHQuery, DddDevice

class AndroidDevice(DddDevice):
    CONTACT_NUMBERS = {
        "John": "0701234567",
        "Lisa": "0709876543",
        "Mary": "0706574839",
        "Andy": None,
    }
    def is_number_valid(self, number):
        if number:
            return True
        return False

    class Call(DeviceAction):
        PARAMETERS = ["selected_contact_to_call.grammar_entry"]
        def perform(self, selected_contact_to_call):
            number = self.device.CONTACT_NUMBERS.get(selected_contact_to_call)
            # TODO: Implement calling
            success = True
            return success

    class ContactRecognizer(EntityRecognizer):
        def recognize_entity(self, string):
            result = []
            words = string.lower().split()
            for contact in self.device.CONTACT_NUMBERS.keys():
                if contact.lower() in words:
                    recognized_entity = {
                        "sort": "contact",
                        "grammar_entry": contact
                    }
                    result.append(recognized_entity)
            return result
            
    class CallerNumberAvailable(Validity):
        PARAMETERS = ["selected_contact_to_call.grammar_entry"]
        def is_valid(self, contact):
            number = self.device.CONTACT_NUMBERS.get(contact)
            return self.device.is_number_valid(number)

    class PhoneNumberAvailable(Validity):
        PARAMETERS = ["selected_contact_of_phone_number.grammar_entry"]
        def is_valid(self, contact):
            number = self.device.CONTACT_NUMBERS.get(contact)
            return self.device.is_number_valid(number)

    class phone_number_of_contact(DeviceWHQuery):
        PARAMETERS = ["selected_contact_of_phone_number.grammar_entry"]
        def perform(self, selected_contact_of_phone_number):
            number = self.device.CONTACT_NUMBERS.get(selected_contact_of_phone_number)
            if not self.device.is_number_valid(number):
                return []

            number_entity = {
                "grammar_entry": number
            }
            return [number_entity]
