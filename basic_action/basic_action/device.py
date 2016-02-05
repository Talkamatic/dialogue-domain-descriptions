from tdm.tdmlib import EntityRecognizer, DeviceAction

class BasicActionDevice:
    CONTACT_NUMBERS = {
        "John": "0701234567",
        "Lisa": "0709876543",
        "Mary": "0706574839",
        "Andy": "0707192837",
    }
    class Call(DeviceAction):
        PARAMETERS = ["selected_contact.grammar_entry"]
        def perform(self, selected_contact):
            number = self.device.CONTACT_NUMBERS[selected_contact]
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
