import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlImage

from DITagger import ImageModel
import os.path


class ImageWindow(ImageModel.ImageModel, BaseWidget):
    def __init__(self, path, file):
        ImageModel.ImageModel.__init__(self, path, file)
        BaseWidget.__init__(self, 'Image window')
        print(path + file)

        # Definition of the forms fields
        self._ditimage = ControlImage()
        self._ditimage.value = path + file

        self._ditid = ControlText('Patient ID')
        ControlText('Patient ID').value = self._usercomment['ditid']

        self._lesion = ControlText('Lesion')
        ControlText('Lesion').value = self._usercomment['lesion']

        self._diagnosis = ControlText('Diagnosis')
        ControlText('Diagnosis').value = self._usercomment['diagnosis']

        self._location = ControlText('Location')
        ControlText('Location').value = self._usercomment['location']

        self._ditcomment = ControlText('Comment')
        ControlText('Comment').value = self._usercomment['ditcomment']

        self._buttonImage = ControlButton('Save Tags')

        self._formset = ['_ditimage', '_ditid', '_lesion', '_diagnosis', '_location', '_ditcomment', '_buttonImage',
                         'by www.dermatologist.co.in']

        # Define the button action
        self._buttonImage.value = self.__buttonAction

    def __buttonAction(self):
        return
        # In case the window has a parent
        # if self.parent!=None: self.parent.addPerson(self)


# Execute the application
# if __name__ == "__main__":   pyforms.startApp(ImageWindow)
