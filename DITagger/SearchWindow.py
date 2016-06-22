import fnmatch
import os

from pyforms import BaseWidget
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlList
from pyforms.Controls import ControlText

from DITagger import ImageModel
from DITagger import SettingsModel


class SearchWindow(ImageModel.ImageModel, SettingsModel.SettingsModel, BaseWidget):
    def __init__(self):
        BaseWidget.__init__(self, 'Search window')
        SettingsModel.SettingsModel.__init__(self)

        self.load()

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

    # Ref: Stackoverflow: 2186525
    def __buttonSearchAction(self):
        _folderList = self.get_setting('folders')
        for _folder in _folderList:
            for root, dirnames, filenames in os.walk(_folder):
                for filename in fnmatch.filter(filenames, '*.jpg'):
                    super(ImageModel.ImageModel, self).__setattr__ \
                        ('fullpath', os.path.join(root, filename))
                    if self.hasIt(self._search.value):
                        self._results += [filename]
        # In case the window has a parent
        # if self.parent!=None: self.parent.addPerson(self)

# Execute the application
# if __name__ == "__main__":   pyforms.startApp(ImageWindow)
