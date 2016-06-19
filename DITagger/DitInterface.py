#!/usr/bin/python

__author__ = "Ricardo Ribeiro"
__credits__ = ["Ricardo Ribeiro"]
__license__ = "MIT"
__version__ = "0.0"
__maintainer__ = "Ricardo Ribeiro"
__email__ = "ricardojvr@gmail.com"
__status__ = "Development"

import pyforms
from   pyforms import BaseWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlButton


class DitInterface(BaseWidget):
    def __init__(self):
        super(DitInterface, self).__init__('Dermatology Image Tagger by Bell R Eapen')

        # Definition of the forms fields
        self._firstname = ControlText('First name', 'Default value')
        self._middlename = ControlText('Middle name')
        self._lastname = ControlText('Lastname name')
        self._fullname = ControlText('Full name')
        self._button = ControlButton('Press this button')

        self._formset = [{
            'Tab1': ['_firstname', '||', '_middlename', '||', '_lastname'],
            'Tab2': ['_fullname']
        },
            '=', (' ', '_button', ' ')]

        self._fullname.addPopupSubMenuOption('Path',
                                             {
                                                 'Delete': self.__dummyEvent,
                                                 'Edit': self.__dummyEvent,
                                                 'Interpolate': self.__dummyEvent
                                             })

        # Define the window main menu using the property main menu
        self.mainmenu = [
            {'File': [
                {'Open': self.__dummyEvent},
                '-',
                {'Save': self.__dummyEvent},
                {'Save as': self.__dummyEvent}
            ]
            },
            {'Edit': [
                {'Copy': self.__dummyEvent},
                {'Past': self.__dummyEvent}
            ]
            }
        ]

    def __dummyEvent(self):
        print ("Menu option selected")


##################################################################################################################
##################################################################################################################
##################################################################################################################

# Execute the application
if __name__ == "__main__":     pyforms.startApp(DitInterface)
