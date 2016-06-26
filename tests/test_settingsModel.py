from unittest import TestCase

from DITagger import model


class TestSettingsModel(TestCase):
    def setUp(self):
        self.settingsModel = model.SettingsModel()

    def test_loadShouldNotThrowError(self):
        self.settingsModel.load()
