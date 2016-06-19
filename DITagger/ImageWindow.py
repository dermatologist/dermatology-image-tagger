import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from   pyforms.Controls import ControlImage


class ImageWindow(BaseWidget):
    def __init__(self):
        # Person.__init__(self, '', '', '')
        BaseWidget.__init__(self, 'Image window')

        # Definition of the forms fields
        self._ditimage = ControlImage()
        self._ditid = ControlText('Patient ID')
        self._lesion = ControlText('Lesion')
        self._diagnosis = ControlText('Diagnosis')
        self._location = ControlText('Location')
        self._ditcomment = ControlText('Comments')
        self._buttonImage = ControlButton('Save Image')

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
