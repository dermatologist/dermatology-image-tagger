import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlImage

from DITagger import ImageModel
import os.path


class ImageWindow(ImageModel.ImageModel, BaseWidget):
    def __init__(self, ditpath, ditfile):
        ImageModel.ImageModel.__init__(self, ditpath, ditfile)
        BaseWidget.__init__(self, 'Image window')

        # Definition of the forms fields
        self._ditimage = ControlImage()
        self._ditimage.value = self._ditpath + self._ditfile

        self._ditid = ControlText('Patient ID')
        self._ditid.value = super(ImageModel.ImageModel, self).__getattribute__('ditid')

        self._lesion = ControlText('Lesion')
        ControlText('Lesion').value = self._usercomment['lesion']

        self._diagnosis = ControlText('Diagnosis')
        ControlText('Diagnosis').value = self._usercomment['diagnosis']

        self._location = ControlText('Location')
        ControlText('Location').value = self._usercomment['location']

        self._ditcomment = ControlText('Comment')
        ControlText('Comment').value = self._usercomment['ditcomment']

        self._buttonSave = ControlButton('Save Tags')
        self._buttonLoad = ControlButton('Load Tags')

        self._formset = ['_ditimage', '_ditid', '_lesion', '_diagnosis', '_location', '_ditcomment', '_buttonSave',
                         '_buttonLoad', 'by www.dermatologist.co.in']

        # Define the button action
        self._buttonSave.value = self.__buttonSaveAction
        self._buttonLoad.value = self.__buttonLoadAction

    def __buttonLoadAction(self):
        # imageModel = ImageModel.ImageModel(self._ditpath, self._ditfile)
        # imageModel.ditid = self._usercomment['ditid']
        self._ditid.value = super(ImageModel.ImageModel, self).__getattribute__('ditid')

    def __buttonSaveAction(self):
        # self._usercomment['ditid'] = ControlText('Patient ID').value
        # self._usercomment['lesion'] = ControlText('Lesion').value
        # self._usercomment['diagnosis'] = ControlText('Diagnosis').value
        # self._usercomment['location'] = ControlText('Location').value
        # self._usercomment['ditcomment'] = ControlText('Comment').value
        super(ImageModel.ImageModel, self).__setattr__('ditid', self._ditid.value)
        # In case the window has a parent
        # if self.parent!=None: self.parent.addPerson(self)


# Execute the application
# if __name__ == "__main__":   pyforms.startApp(ImageWindow)
