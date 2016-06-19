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
from   pyforms.Controls import ControlImage
from   pyforms.Controls import ControlButton


class DitInterface(BaseWidget):
    def __init__(self):
        super(DitInterface, self).__init__('Dermatology Image Tagger by Bell R Eapen')

        # Definition of the forms fields
        self._ditimage = ControlImage()
        self._ditid = ControlText('Patient ID')
        self._lesion = ControlText('Lesion')
        self._diagnosis = ControlText('Diagnosis')
        self._location = ControlText('Location')
        self._ditcomment = ControlText('Comments')
        self._buttonImage = ControlButton('Save Image')

        """
        self._formset = [{
            'Image': ['_ditimage', '||', '_ditid', '||', '_lesion', '_diagnosis', '||', '_location', '||', '_ditcomment', '||', '_buttonImage'],
            'Search': ['_fullname'],
            'Settings': ['_fullname'],
            'Help/Avout': ['_fullname']
        },
            '=', (' ', '_buttonExit', ' ')]

        self._ditid.addPopupSubMenuOption('Path',
                                             {
                                                 'Delete': self.__dummyEvent,
                                                 'Edit': self.__dummyEvent,
                                                 'Interpolate': self.__dummyEvent
                                             })
        """

        # Define the window main menu using the property main menu
        self.mainmenu = [
            {'File': [
                {'Open': self.__dummyEvent},
                '-',
                {'Save': self.__dummyEvent},
                {'Restore': self.__dummyEvent},
                {'Import': self.__dummyEvent},
                '-',
                {'Exit': self.__dummyEvent}

            ]
            },
            {'Edit': [
                {'Paint': self.__dummyEvent},
                {'Rectangle': self.__dummyEvent}
            ]
            },
            {'Search': [
                {'Find': self.__dummyEvent},
                {'Find in Folder': self.__dummyEvent}
            ]
            },
            {'Settings': [
                {'Default Path': self.__dummyEvent},
                {'Encryption': self.__dummyEvent},
                {'Back Up': self.__dummyEvent}

            ]
            },
            {'Help/About': [
                {'Help/About': self.__dummyEvent},
                {'Check for Updates': self.__dummyEvent}
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
