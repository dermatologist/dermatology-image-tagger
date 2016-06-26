import os.path
from unittest import TestCase

from DITagger import model


class TestImageModel(TestCase):
    def setUp(self):
        self.imageModel = model.ImageModel()
        self.imageModel.fullpath = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'test1.JPG'
        self.imageModel.ditid = 'Patient'
        self.imageModel.lesion = 'Papule'
        self.imageModel.diagnosis = 'Lichen Planus'
        self.imageModel.location = 'Wrist'
        self.imageModel.ditcomment = 'Self Limiting'
        self.imageModel.ditsave()

    def tearDown(self):
        self.imageModel = model.ImageModel()
        self.imageModel.fullpath = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'test1.JPG'
        self.imageModel.ditid = ''
        self.imageModel.lesion = ''
        self.imageModel.diagnosis = ''
        self.imageModel.location = ''
        self.imageModel.ditcomment = ''
        self.imageModel.ditsave()

    def test_ditid(self):
        self.imageModel.fullpath = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'test1.JPG'
        self.assertEqual(self.imageModel.ditid, 'Patient', 'id tag test')
        self.assertTrue(self.imageModel.hasIt('Patient'))

    def test_lesion(self):
        self.imageModel.fullpath = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'test1.JPG'
        self.assertEqual(self.imageModel.lesion, 'Papule', 'Lesion Test')
        self.assertTrue(self.imageModel.hasIt('Papule'))

    def test_diagnosis(self):
        self.imageModel.fullpath = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'test1.JPG'
        self.assertEqual(self.imageModel.diagnosis, 'Lichen Planus', 'Diagnosis Test')
        self.assertTrue(self.imageModel.hasIt('Lichen Planus'))

    def test_location(self):
        self.imageModel.fullpath = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'test1.JPG'
        self.assertEqual(self.imageModel.location, 'Wrist', 'Location Test')
        self.assertTrue(self.imageModel.hasIt('Wrist'))

    def test_ditcomment(self):
        self.imageModel.fullpath = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'test1.JPG'
        self.assertEqual(self.imageModel.ditcomment, 'Self Limiting', 'Comment Test')
        self.assertTrue(self.imageModel.hasIt('Self Limiting'))
