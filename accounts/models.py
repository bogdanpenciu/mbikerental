from django.contrib.auth.models import User
from django.db import models
from django.db.models import OneToOneField

genders = (('M', 'masculine'),
           ('F', 'feminine'))

class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=1)
    gender = models.CharField(choices=genders, max_length=15, null=True, blank=True)
    picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    accepted_terms = models.BooleanField(default=False)

    def __str__(self):
     return f'{self.user.username} Profile'