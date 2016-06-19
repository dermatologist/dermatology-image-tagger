import pickle


class FolderModel(object):
    def __init__(self):
        self._folders = []

    def addFolder(self, folder):
        self._folders.append(folder)

    def removeFolder(self, index):
        return self._folders.pop(index)

    def save(self, filename):
        output = open(filename, 'wb')
        pickle.dump(self._folders, output)

    def load(self, filename):
        pkl_file = open(filename, 'rb')
        self._folders = pickle.load(pkl_file)
