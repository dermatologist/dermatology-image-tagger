import pickle


class SettingsModel(object):
    def __init__(self):
        self._settings = {}
        self._filename = 'settings.ini'

    def add_setting(self, key, value):
        self._settings[key] = value

    def get_setting(self, key):
        return self._settings[key]

    def save(self):
        output = open(self._filename, 'wb')
        pickle.dump(self._settings, output)

    def load(self):
        pkl_file = open(self._filename, 'rb')
        self._settings = pickle.load(pkl_file)
