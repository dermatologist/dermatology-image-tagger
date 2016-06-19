from unittest import TestCase
from DITagger import ImageModel
import os.path


class TestImageModel(TestCase):
    def setUp(self):
        imageModel = ImageModel.ImageModel(os.path.dirname(os.path.abspath(__file__)), '/test1.JPG')
        imageModel.ditid = 'Patient'
        imageModel.lesion = 'Papule'
        imageModel.diagnosis = 'Lichen Planus'
        imageModel.location = 'Wrist'
        imageModel.ditcomment = 'Self Limiting'

    def tearDown(self):
        imageModel = ImageModel.ImageModel(os.path.dirname(os.path.abspath(__file__)), '/test1.JPG')
        imageModel.ditid = ''
        imageModel.lesion = ''
        imageModel.diagnosis = ''
        imageModel.location = ''
        imageModel.ditcomment = ''

    def test_ditid(self):
        imageModel = ImageModel.ImageModel(os.path.dirname(os.path.abspath(__file__)), '/test1.JPG')
        self.assertEqual(imageModel.ditid, 'Patient', 'id tag test')
        self.assertTrue(imageModel.hasIt('Patient'))

    def test_lesion(self):
        imageModel = ImageModel.ImageModel(os.path.dirname(os.path.abspath(__file__)), '/test1.JPG')
        self.assertEqual(imageModel.lesion, 'Papule', 'Lesion Test')
        self.assertTrue(imageModel.hasIt('Papule'))

    def test_diagnosis(self):
        imageModel = ImageModel.ImageModel(os.path.dirname(os.path.abspath(__file__)), '/test1.JPG')
        self.assertEqual(imageModel.diagnosis, 'Lichen Planus', 'Diagnosis Test')
        self.assertTrue(imageModel.hasIt('Lichen Planus'))

    def test_location(self):
        imageModel = ImageModel.ImageModel(os.path.dirname(os.path.abspath(__file__)), '/test1.JPG')
        self.assertEqual(imageModel.location, 'Wrist', 'Location Test')
        self.assertTrue(imageModel.hasIt('Wrist'))

    def test_ditcomment(self):
        imageModel = ImageModel.ImageModel(os.path.dirname(os.path.abspath(__file__)), '/test1.JPG')
        self.assertEqual(imageModel.ditcomment, 'Self Limiting', 'Comment Test')
        self.assertTrue(imageModel.hasIt('Self Limiting'))
