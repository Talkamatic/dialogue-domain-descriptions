# -*- coding: utf-8 -*-

from tdm.lib.device import DeviceAction, DddDevice


class ContactBookDevice(DddDevice):

    class ReportCall(DeviceAction):
        def perform(self, selected_contact):
            return True
