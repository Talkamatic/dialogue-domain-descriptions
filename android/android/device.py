from tdm.tdmlib import EntityRecognizer, DeviceAction, Validity
from tdm.device_handler import send_to_frontend_device

class AndroidDevice:
    class Call(DeviceAction):
        PARAMETERS = ["selected_contact.grammar_entry"]
        @send_to_frontend_device
        def perform(self, selected_contact):
            pass

    class ContactRecognizer(EntityRecognizer):
        @send_to_frontend_device
        def recognize_entity(self, string):
            pass

    class PhoneNumberAvailable(Validity):
        PARAMETERS = ["selected_contact.grammar_entry"]
        @send_to_frontend_device
        def is_valid(self, selected_contact):
            pass
