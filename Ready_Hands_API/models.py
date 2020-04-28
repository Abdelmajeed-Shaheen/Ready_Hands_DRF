from django.db import models
from django.contrib.auth.models import User

""" Adders Model """
class Address(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    street = models.CharField(max_length = 120)
    building_no = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    class Meta:
        verbose_name_plural = "Addresses"
    def __str__(self):
        return f'{self.user.username}, {self.street}'


""" Client Model """
class Client(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = models.ImageField(blank = True , null = True)
    phone_no = models.TextField(verbose_name="phone_no")
    class Meta:
        verbose_name_plural = "Clients"
    def __str__(self):
        return self.user.username


""" Worker Model """
class Worker(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    image = models.ImageField(blank = True , null = True)
    phone_no = models.TextField(verbose_name="phone_no")
    hour_rate = models.DecimalField(max_digits=4, decimal_places=2)
    rating = models.ManyToManyField("Review",through = "WorkerReview")
    class Meta:
        verbose_name_plural = "Workers"
    def __str__(self):
        return self.user.username


""" Service Model """
class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    class Meta:
        verbose_name_plural = "Services"
    def __str__(self):
        return self.title


""" WorkerJob Model """
class WorkerJob(models.Model):
    worker = models.ForeignKey(Worker,on_delete = models.CASCADE)
    job = models.ForeignKey("Job",on_delete = models.CASCADE)


""" Job Model """
class Job(models.Model):
    MALE = "M"
    FEMALE = "F"
    PENDING = "P"
    SELECTED = "S"
    FINISHED = "FI"
    GENDER = [(MALE , "MALE"),(FEMALE , "FEMALE")]
    STATUS = [(PENDING,"PENDING"),(SELECTED,"SELECTED"),(FINISHED,"FINISHED")]
    title = models.CharField(max_length=120)
    client = models.ForeignKey(Client,on_delete = models.CASCADE)
    service = models.ForeignKey(Service,on_delete = models.CASCADE)
    worker = models.ManyToManyField(Worker,through = WorkerJob )
    address = models.ForeignKey(Address,on_delete= models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    rating_range = models.DecimalField(max_digits=2, decimal_places=1)
    date_from = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_to = models.DateTimeField(auto_now=False, auto_now_add=False)
    no_of_workers = models.IntegerField()
    gender = models.CharField(choices = GENDER , max_length = 2,default = MALE)
    status =models.CharField(choices = STATUS , max_length = 3,default = PENDING)
    selected_worker = models.ForeignKey(User,on_delete =models.CASCADE,blank = True , null = True)
    class Meta:
        verbose_name_plural = "Jobs"
    def __str__(self):
        return self.title


""" WorkerReview Model """
class WorkerReview(models.Model):
    review = models.ForeignKey("Review" , on_delete = models.CASCADE)
    worker = models.ForeignKey(Worker , on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.review.rating}'


""" Review Model """
class Review(models.Model):
    reviewed_by = models.ForeignKey(Client,on_delete = models.CASCADE)
    reviewed = models.ForeignKey(Worker,on_delete = models.CASCADE)
    content = models.CharField(max_length = 400)
    rating = models.DecimalField(max_digits = 2 , decimal_places = 1)
    class Meta:
        verbose_name_plural = "Reviews"
    def __str__(self):
        return f'{self.reviewed_by} rated {self.reviewed}'
