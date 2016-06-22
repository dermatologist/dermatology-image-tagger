from pyforms import BaseWidget
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlList
from pyforms.Controls import ControlText

from DITagger import SettingsModel


class SearchWindow(SettingsModel.SettingsModel, BaseWidget):
    def __init__(self):
        BaseWidget.__init__(self, 'Search window')
        SettingsModel.SettingsModel.__init__(self)
        SettingsModel.SettingsModel.load()

        # Definition of the forms fields
        self._search = ControlText('Search')
        self._buttonSearch = ControlButton('Search')
        self._results = ControlList('Search')
        self._results.horizontalHeaders = ['Image', 'Date Taken', 'Patient ID', 'Lesion',
                                           'Diagnosis', 'Location', 'Comment', 'Tag Date']
        self._results.selectEntireRow = True
        self._formset = ['_search', '_buttonSearch', '_results', 'by www.dermatologist.co.in']

        # Define the button action
        self._buttonSearch.value = self.__buttonSearchAction
        # self._buttonLoad.value = self.buttonLoadAction

    def __buttonSearchAction(self):
        _folderList = self.get_setting('folders')
        for _folder in _folderList:
            return
        # In case the window has a parent
        # if self.parent!=None: self.parent.addPerson(self)

# Execute the application
# if __name__ == "__main__":   pyforms.startApp(ImageWindow)
