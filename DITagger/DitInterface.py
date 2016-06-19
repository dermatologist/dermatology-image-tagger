#!/usr/bin/python

__author__ = "Bell Eapen"
__credits__ = ["Bell Eapen"]
__license__ = "GPL"
__version__ = "0.2.0"
__maintainer__ = "Bell Eapen"
__email__ = "github@gulfdoctor.net"
__status__ = "Development"

import pyforms
from   pyforms import BaseWidget
from   pyforms.Controls import ControlEmptyWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlImage
from   pyforms.Controls import ControlButton

from DITagger import ImageWindow
import os.path

class DitInterface(BaseWidget):
    def __init__(self):
        super(DitInterface, self).__init__('Dermatology Image Tagger by Bell R Eapen')
        self._panel = ControlEmptyWidget()

        ##Image Window
        self._win = ImageWindow.ImageWindow(os.path.dirname(os.path.abspath(__file__)), '/blank.jpg')
        self._win.parent = self
        self._panel.value = self._win

        """
        # Definition of the forms fields
        self._ditimage = ControlImage()
        self._ditid = ControlText('Patient ID')
        self._lesion = ControlText('Lesion')
        self._diagnosis = ControlText('Diagnosis')
        self._location = ControlText('Location')
        self._ditcomment = ControlText('Comments')
        self._buttonImage = ControlButton('Save Image')


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
                {'Open': self.__fileOpen},
                '-',
                {'Save': self.__dummyEvent},
                {'Restore': self.__dummyEvent},
                {'Import': self.__dummyEvent},
                '-',
                {'Exit': self.__exit}

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

    def __exit(self):
        exit(0)

    def __fileOpen(self):
        self.loadWindow()

    def loadWindowData(self, filename):
        print ("Open option selected: " + filename)


##################################################################################################################
##################################################################################################################
##################################################################################################################

# Execute the application
if __name__ == "__main__":     pyforms.startApp(DitInterface)
