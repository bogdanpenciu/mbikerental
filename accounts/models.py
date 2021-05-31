from datetime import datetime
from dateutil import relativedelta

from django.contrib.auth.models import User
from django.db import models
from django.db.models import OneToOneField

import datetime


categories = (('AM', 'AM'),
            ('A1', 'A1'),
              ('A2', 'A2'),
              ('A', 'A'))

class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(default=datetime.date.today)
    licence_valid_date = models.DateField(default=datetime.date.today)
    licence_cat = models.CharField(default='A', choices=categories, max_length=15, null=True, blank=True)
    picture = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)

    def licence_old(self):
        today = datetime.date.today()
        date2 = self.licence_valid_date
        diff = relativedelta.relativedelta(today, date2)
        years = diff.years
        months = diff.months
        return f'{years} Years {months} Months'


    def __str__(self):
     return f'{self.user.username} Profile'