class ImageModel(object):
    """
    Image Model for the DITagger.
    The Class will write to the image file
    """

    def __init__(self, ditpath, ditfile):
        self._ditpath = ditpath
        self._ditfile = ditfile

    @property
    def ditpath(self):
        return self._ditpath

    @ditpath.setter
    def ditpath(self, ditpath):
        self._ditpath = ditpath

    @property
    def ditfile(self):
        return self._ditfile

    @ditfile.setter
    def ditfile(self, ditfile):
        self._ditfile = ditfile

    @property
    def ditid(self):
        return self._ditid

    @ditid.setter
    def ditid(self, ditid):
        self._ditid = ditid

    @property
    def lesion(self):
        return self._lesion

    @lesion.setter
    def lesion(self, lesion):
        self._lesion = lesion

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def lesion(self, diagnosis):
        self._diagnosis = diagnosis

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def ditcomment(self):
        return self._ditcomment

    @ditcomment.setter
    def ditcomment(self, ditcomment):
        self._ditcomment = ditcomment
