__author__ = 'vijay'
from storages.backends import s3boto

class MyS3BotoStorage(s3boto.S3BotoStorage):
    def path(self, name):
        return self._normalize_name(name)

