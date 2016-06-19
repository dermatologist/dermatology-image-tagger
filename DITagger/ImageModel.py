import pexif

import json

class ImageModel(object):
    """
    Image Model for the DITagger.
    The Class will write to the image file
    Ref: stackoverflow 8586940 writing-complex-custom-metadata-on-images-through-python
    Ref: https://pypi.python.org/pypi/piexif
    Ref: stackoverflow 10833928
    """

    def __init__(self, ditpath, ditfile):
        self._ditpath = ditpath
        self._ditfile = ditfile

        # Add exif in a file
        self._img = pexif.JpegFile.fromFile(ditpath + ditfile)
        self._img.exif.primary.ImageDescription = "DITagger"
        self._usercomment = json.loads(self._img.exif.primary.ExtendedEXIF.UserComment)

        """
        self._usercomment = {
            'ditid': '',
            'lesion': '',
            'diagnosis': '',
            'location': '',
            'ditcomment': ''
        }
        """

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
        return self._usercomment['ditid']

    @ditid.setter
    def ditid(self, ditid):
        self._usercomment['ditid'] = ditid;

    @property
    def lesion(self):
        return self._usercomment['lesion']

    @lesion.setter
    def lesion(self, lesion):
        self._usercomment['lesion'] = lesion;

    @property
    def diagnosis(self):
        return self._usercomment['diagnosis']

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        self._usercomment['diagnosis'] = diagnosis

    @property
    def location(self):
        return self._usercomment['location']

    @location.setter
    def location(self, location):
        self._usercomment['location'] = location

    @property
    def ditcomment(self):
        return self._usercomment['ditcomment']

    @ditcomment.setter
    def ditcomment(self, ditcomment):
        self._usercomment['ditcomment'] = ditcomment

    def _ditsave(self):
        self._img.exif.primary.ExtendedEXIF.UserComment = json.dumps(self._usercomment)
        self._img.writeFile(self._ditpath + self._ditfile)

    def hasIt(self, needle):
        if needle in self._usercomment:
            return True
        else:
            return False
