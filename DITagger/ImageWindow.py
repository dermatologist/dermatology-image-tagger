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
        self._lesion.value = super(ImageModel.ImageModel, self).__getattribute__('lesion')

        self._diagnosis = ControlText('Diagnosis')
        self._diagnosis.value = super(ImageModel.ImageModel, self).__getattribute__('diagnosis')

        self._location = ControlText('Location')
        self._location.value = super(ImageModel.ImageModel, self).__getattribute__('location')

        self._ditcomment = ControlText('Comment')
        self._ditcomment.value = super(ImageModel.ImageModel, self).__getattribute__('ditcomment')


        self._buttonSave = ControlButton('Save Tags')

        self._formset = ['_ditimage', '_ditid', '_lesion', '_diagnosis', '_location', '_ditcomment', '_buttonSave',
                         'by www.dermatologist.co.in']

        # Define the button action
        self._buttonSave.value = self.__buttonSaveAction

    def __buttonSaveAction(self):

    def __buttonSaveAction(self):
        self._ditimage.value = self._ditpath + self._ditfile
        super(ImageModel.ImageModel, self).__setattr__('ditid', self._ditid.value)
        super(ImageModel.ImageModel, self).__setattr__('lesion', self._lesion.value)
        super(ImageModel.ImageModel, self).__setattr__('diagnosis', self._diagnosis.value)
        super(ImageModel.ImageModel, self).__setattr__('location', self._location.value)
        super(ImageModel.ImageModel, self).__setattr__('ditcomment', self._ditcomment.value)
        self.ditsave()
        # In case the window has a parent
        # if self.parent!=None: self.parent.addPerson(self)


# Execute the application
# if __name__ == "__main__":   pyforms.startApp(ImageWindow)
