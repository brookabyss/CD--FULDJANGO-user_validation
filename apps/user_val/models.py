from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def check_length(self,postData):
        if len(postData)<8 or len(postData)>26:
            return False
        return True
    

class Users(models.Model):
    username=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
    def __str__(self):
        return self.username
