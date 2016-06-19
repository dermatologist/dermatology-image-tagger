from unittest import TestCase
from preggy import expect
from DITagger import ImageModel


class TestImageModel(TestCase):
    def test_ditid(self):
        imageModel = ImageModel.ImageModel('', '/test1.JPG')
        print(imageModel.ditpathfile)
        self.assertEqual(self, imageModel._ditpath, '../tests/', 'incorrect filename')
