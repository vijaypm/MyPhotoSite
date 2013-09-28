from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import time

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=80)
#     hash_pwd = models.CharField(max_length=64) # SHA-256 of password
#     email = models.CharField(max_length=80)
#     created_dt = models.DateTimeField(default=timezone.now())
#     modified_dt = models.DateTimeField(null=True)
#     verified = models.BooleanField(default=False) # indicates is user has confirmed registration or not
#     verify_code = models.CharField(max_length=255) # verification code to confirm registration
#     verified_dt = models.DateTimeField(null=True)
#
#     def __init__(self, *args, **kwargs):
#         super(User, self).__init__(*args, **kwargs)
#         self.modified_dt = timezone.now()
#
#     def __unicode__(self):
#         return self.username

class UserAlbum(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=80)
    created_dt = models.DateTimeField(default=timezone.now())
    modified_dt = models.DateTimeField(null=True)

    def __init__(self, *args, **kwargs):
        super(UserAlbum, self).__init__(*args, **kwargs)
        self.modified_dt = timezone.now()

    def __unicode__(self):
        return self.name + ' by ' + self.user.username

def uploadPath(instance, filename):
    return 'images/%s/%s/%s'%(instance.album.id,time.strftime('%Y/%m/%d', time.gmtime()),filename)

class AlbumPhoto(models.Model):
    album = models.ForeignKey(UserAlbum)
    filename = models.CharField(max_length=80)
    created_dt = models.DateTimeField(default=timezone.now())
    modified_dt = models.DateTimeField(null=True)
    tags = models.TextField(null=True, blank=True) # convert to JSONField later http://djangosnippets.org/snippets/377/
    imageFile = models.ImageField(upload_to=uploadPath)

    def __init__(self, *args, **kwargs):
        super(AlbumPhoto, self).__init__(*args, **kwargs)
        self.modified_dt = timezone.now()

    def __unicode__(self):
        return self.filename + ' in ' + self.album

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.imageFile.storage, self.imageFile.path
        # Delete the model before the file
        super(AlbumPhoto, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

