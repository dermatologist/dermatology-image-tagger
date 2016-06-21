import pexif
import piexif
import json

class ImageModel(object):
    """
    Image Model for the DITagger.
    The Class will write to the image file
    Ref: stackoverflow 8586940 writing-complex-custom-metadata-on-images-through-python
    Ref: https://pypi.python.org/pypi/piexif
    Ref: stackoverflow 10833928
    """

    @property
    def fullpath(self):
        return self._fullpath

    @fullpath.setter
    def fullpath(self, fullpath):
        self._fullpath = fullpath
        self._img = pexif.JpegFile.fromFile(self._fullpath)
        self._img.exif.primary.ImageDescription = "DITagger"
        # TODO: Create backup if ImageDescription is not DITagger
        _exif_dict = piexif.load(self._fullpath)
        try:
            self._usercomment = json.loads(_exif_dict["Exif"][37510])
        except:
            self._usercomment = {
                'ditid': '',
                'lesion': '',
                'diagnosis': '',
                'location': '',
                'ditcomment': '',
                'ditdate': ''
            }

    @property
    def ditid(self):
        return self._usercomment['ditid']

    @ditid.setter
    def ditid(self, ditid):
        self._usercomment['ditid'] = ditid

    @property
    def lesion(self):
        return self._usercomment['lesion']

    @lesion.setter
    def lesion(self, lesion):
        self._usercomment['lesion'] = lesion

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

    @property
    def ditdate(self):
        return self._usercomment['ditdate']

    @ditdate.setter
    def ditdate(self, ditdate):
        self._usercomment['ditdate'] = ditdate

    def ditsave(self):
        # Save image using pexif
        # Ref: https://github.com/bennoleslie/pexif
        self._img.exif.primary.ExtendedEXIF.UserComment = json.dumps(self._usercomment)
        self._img.writeFile(self._fullpath)

    def hasIt(self, needle):
        if needle in json.dumps(self._usercomment):
            return True
        else:
            return False
