from pyforms import BaseWidget
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlDir
from pyforms.Controls import ControlLabel
from pyforms.Controls import ControlList

from DITagger import SettingsModel


class SettingsWindow(SettingsModel.SettingsModel, BaseWidget):
    def __init__(self):
        BaseWidget.__init__(self, 'Settings window')
        SettingsModel.SettingsModel.__init__(self)

        # Definition of the forms fields
        self._folder_label = ControlLabel('Folders to Search')
        self._folders = ControlList('Folders',
                                    plusFunction=self.__addFolderButtonAction,
                                    minusFunction=self.__rmFolderButtonAction)
        self._folder = ControlDir('Select Folder')
        self._buttonSave = ControlButton('Save Settings')
        self._buttonLoad = ControlButton('Load Settings')

        # self._folders.horizontalHeaders = ['Folders']
        self._folders.selectEntireRow = True
        self._formset = ['_folder_label', '_folder', '_folders',
                         '_buttonLoad', '_buttonSave',
                         'by www.dermatologist.co.in']

        # Define the button action
        self._buttonSave.value = self.__buttonSaveAction
        self._buttonLoad.value = self.__buttonLoadAction

    def __addFolderButtonAction(self):
        print self._folder.value
        self._folders += [self._folder.value]

    def __rmFolderButtonAction(self):
        return

    def __buttonSaveAction(self):
        self.save()

    def __buttonLoadAction(self):
        self.load()
        # Define the button action
        # self._buttonSave.value = self.buttonSaveAction
        # self._buttonLoad.value = self.buttonLoadAction

        # In case the window has a parent
        # if self.parent!=None: self.parent.addPerson(self)

# Execute the application
# if __name__ == "__main__":   pyforms.startApp(ImageWindow)
