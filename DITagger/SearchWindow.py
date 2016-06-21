import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlList

from DITagger import ImageModel
import os.path


class SearchWindow(BaseWidget):
    def __init__(self):
        BaseWidget.__init__(self, 'Search window')

        # Definition of the forms fields


        self._search = ControlText('Search')
        self._buttonSearch = ControlButton('Search')
        self._results = ControlList('Search')

        self._formset = ['_search', '_buttonSearch', '_results', 'by www.dermatologist.co.in']

        # Define the button action
        # self._buttonSave.value = self.buttonSaveAction
        # self._buttonLoad.value = self.buttonLoadAction

        # In case the window has a parent
        # if self.parent!=None: self.parent.addPerson(self)

# Execute the application
# if __name__ == "__main__":   pyforms.startApp(ImageWindow)
