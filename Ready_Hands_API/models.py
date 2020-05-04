from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = models.ImageField(blank = True , null = True)
    phone_no = models.TextField(verbose_name="phone_no")

    def __str__(self):
        return self.user.username


class Worker(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = models.ImageField(blank = True , null = True)
    phone_no = models.TextField(verbose_name="phone_no")
    hour_rate = models.DecimalField(max_digits=4, decimal_places=2)
    # on_save signal from review object this gets updated
    rating = models.DecimalField(max_digits=4, decimal_places=2,default=5.0)

    def __str__(self):
        return self.user.username


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title


class Job(models.Model):
    GENDER = [("M" , "MALE"),("F" , "FEMALE")]
    STATUS = [("P","PENDING"),("S","SELECTED"),("FI","FINISHED")]
    title = models.CharField(max_length=120)
    client = models.ForeignKey(Client,on_delete = models.CASCADE)
    service = models.ForeignKey(Service,on_delete = models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # min worker rating
    rating_range = models.DecimalField(max_digits=4, decimal_places=2)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    no_of_workers = models.IntegerField()
    # Prefered gender for workers
    gender = models.CharField(choices = GENDER , max_length = 2, null=True,blank=True)
    status =models.CharField(choices = STATUS , max_length = 3,default = "P")
    class Meta:
        verbose_name_plural = "Jobs"
    def __str__(self):
        return self.title


class Applicant(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    acccepted = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.worker.user.username} , {self.job.title}'

class Review(models.Model):
    reviewed_by = models.ForeignKey(Client,on_delete = models.CASCADE)
    reviewed = models.ForeignKey(Worker,on_delete = models.CASCADE)
    job = models.ForeignKey(Job,on_delete = models.CASCADE)
    content = models.CharField(max_length = 400)
    rating = models.DecimalField(max_digits = 2 , decimal_places = 1)

    def __str__(self):
        return f'{self.reviewed_by} rated {self.reviewed}'
