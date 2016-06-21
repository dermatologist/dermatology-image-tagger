from pyforms import BaseWidget
from pyforms.Controls import ControlLabel
from pyforms.Controls import ControlList


class SettingsWindow(BaseWidget):
    def __init__(self):
        BaseWidget.__init__(self, 'Settings window')

        # Definition of the forms fields
        self._folder_label = ControlLabel('Folders to Search')
        self._folders = ControlList('Folders',
                                    plusFunction=self.__addFolderButtonAction,
                                    minusFunction=self.__rmFolderButtonAction)
        # self._folders.horizontalHeaders = ['Folders']
        self._folders.selectEntireRow = True
        self._formset = ['_folder_label', '_folders', 'by www.dermatologist.co.in']

    def __addFolderButtonAction(self):
        return

    def __rmFolderButtonAction(self):
        return
        # Define the button action
        # self._buttonSave.value = self.buttonSaveAction
        # self._buttonLoad.value = self.buttonLoadAction

        # In case the window has a parent
        # if self.parent!=None: self.parent.addPerson(self)

# Execute the application
# if __name__ == "__main__":   pyforms.startApp(ImageWindow)
