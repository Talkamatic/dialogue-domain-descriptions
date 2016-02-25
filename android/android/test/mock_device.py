from tdm.tdmlib import EntityRecognizer, DeviceAction, Validity, DeviceWHQuery

class AndroidDevice:
    CONTACT_NUMBERS = {
        "John": "0701234567",
        "Lisa": "0709876543",
        "Mary": "0706574839",
        "Andy": None,
    }
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
            
    class PhoneNumberAvailable(Validity):
        PARAMETERS = ["selected_contact_to_call.grammar_entry"]
        def is_valid(self, selected_contact_to_call):
            number = self.device.CONTACT_NUMBERS.get(selected_contact_to_call)
            if number:
                return True
            return False

    class phone_number_of_contact(DeviceWHQuery):
        PARAMETERS = ["selected_contact_of_phone_number.grammar_entry"]
        def perform(self, selected_contact_of_phone_number):
            number = self.device.CONTACT_NUMBERS.get(selected_contact_of_phone_number)
            number_entity = {
                "grammar_entry": number
            }
            return [number_entity]
