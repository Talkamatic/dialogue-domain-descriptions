from tdm.lib.device import EntityRecognizer, DeviceWHQuery, DddDevice

class BasicQueryDevice(DddDevice):
    CONTACT_NUMBERS = {
        "John": "0701234567",
        "Lisa": "0709876543",
        "Mary": "0706574839",
        "Andy": None,
    }
    class phone_number_of_contact(DeviceWHQuery):
        PARAMETERS = ["selected_contact.grammar_entry"]
        def perform(self, selected_contact):
            number = self.device.CONTACT_NUMBERS.get(selected_contact)
            number_entity = {
                "grammar_entry": number
            }
            return [number_entity]

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
