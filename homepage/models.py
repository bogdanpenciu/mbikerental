from django.conf import settings
from django.db import models
from accounts.models import UserProfile, User
from django.utils import timezone

clases = (('AM', 'AM'),
           ('A1', 'A1'),
           ('A2', 'A2'),
           ('A', 'A'))

class Moto(models.Model):
    make = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    power = models.IntegerField()
    price = models.IntegerField()
    picture = models.CharField(max_length=200, null=True)
    license = models.CharField(choices=clases, max_length=20, null=True, blank=True, default='A')
    fuel_usage = models.FloatField(default=0)
    deposit = models.IntegerField(default=500)
    additional_info = models.TextField(max_length=2000, default='')

    def __str__(self):
        return f'{self.make} {self.type}'

    def get_rating(self):
        total = sum(int(review['stars']) for review in self.reviews.values())

        if self.reviews.count() > 0:
            return total/ self.reviews.count()
        else:
            return 3





class PriceIncrease(models.Model):
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    percent1_3 = models.FloatField(default=20)
    percent4_6 = models.FloatField(default=15)
    percent7_13 = models.FloatField(default=10)

    def onetothree(self):
        a= int(self.moto.price +(self.moto.price *(self.percent1_3/100)))
        return a

    def fourtosix(self):
        b=int(self.moto.price +(self.moto.price *(self.percent4_6/100)))
        return b

    def seventothirteen(self):
        c=int(self.moto.price +(self.moto.price *(self.percent7_13/100)))
        return c



    def __str__(self):
        return f'Procent for: {self.moto.make} {self.moto.type}'


class Reservation(models.Model):
    date_reserv = models.DateTimeField(default=timezone.now)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    date_start = models.DateField(null=True, blank=True)
    date_return = models.DateField(null=True, blank=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    # class Meta:
    #     unique_together =['customer','moto']


    def reservation_priod(self):
        x= self.date_return - self.date_start
        return x.days


    def __str__(self):
        return f'Reservation no.{self.id}'

class MotoReview(models.Model):
    moto = models.ForeignKey(Moto, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars= models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.moto.make, self.id)


class Contact(models.Model):
    full_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    e_mail = models.EmailField()
    message = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message: {self.id} from {self.full_name}'



