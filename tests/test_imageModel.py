from unittest import TestCase
from preggy import expect
from DITagger import ImageModel
import os.path


class TestImageModel(TestCase):
    def test_ditid(self):
        imageModel = ImageModel.ImageModel(os.path.dirname(os.path.abspath(__file__)), '/test1.JPG')
        imageModel.ditid = 'BELL'
        imageModel2 = ImageModel.ImageModel(os.path.dirname(os.path.abspath(__file__)), '/test1.JPG')
        self.assertEqual(imageModel2.ditid, 'BELL', 'id tag test')
        self.assertTrue(imageModel.hasIt('BELL'))
