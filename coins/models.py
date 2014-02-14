import datetime, boto
from django.db import models
from django.utils import timezone

# Create your models here.
class Location(models.Model):
    name             = models.CharField(max_length=200)
    lat              = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    lon              = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    def __unicode__(self):
        return self.name

class Coin(models.Model):
    ERAS = (
        ('RR', 'Roman Republican'),
        ('RI', 'Roman Imperial'),
        ('GA', 'Greek Archaic'),
        ('GC', 'Greek Classical'),
        ('GH', 'Greek Hellenistic'),
    )

    title             = models.CharField(max_length=200)
    pub_date          = models.DateTimeField(auto_now_add=True)
    date_start        = models.IntegerField(default=0, null=True)
    date_end          = models.IntegerField(default=0, null=True)
    denomination      = models.CharField(max_length=50, null=True)
    minting_authority = models.CharField(max_length=200, null=True)
    bibliography      = models.CharField(max_length=200, null=False)
    era               = models.CharField(max_length=2, choices=ERAS, null=True)
    mint_location     = models.ForeignKey(Location, default=0, related_name="mint")
    find_location     = models.ForeignKey(Location, default=0, related_name="find")

    description       = models.TextField()

    image1            = models.ImageField(upload_to="images", default="static/coins/images/default_coin_image.jpeg")
    image2            = models.ImageField(upload_to="images", default="static/coins/images/default_coin_image.jpeg")
    image3            = models.ImageField(upload_to="images", default="static/coins/images/default_coin_image.jpeg")
    image4            = models.ImageField(upload_to="images", default="static/coins/images/default_coin_image.jpeg")
    image5            = models.ImageField(upload_to="images", default="static/coins/images/default_coin_image.jpeg")

    def __unicode__(self):
        return self.title
    
    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date < now

class Tag(models.Model):
    title             = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class coin_has_tag(models.Model):
    tag               = models.ForeignKey(Tag, default="tester")
    coin              = models.ForeignKey(Coin, default="tester")

class Corpus(models.Model):
    title             = models.CharField(max_length=100)
    date_created      = models.DateTimeField('date created')
    description       = models.CharField(max_length=500, null=True)

    content           = models.TextField()

    image1            = models.ImageField(upload_to="images", default="static/coins/images/default_coin_image.jpeg")
    image2            = models.ImageField(upload_to="images", default="static/coins/images/default_coin_image.jpeg")
    image3            = models.ImageField(upload_to="images", default="static/coins/images/default_coin_image.jpeg")
    image4            = models.ImageField(upload_to="images", default="static/coins/images/default_coin_image.jpeg")
    image5            = models.ImageField(upload_to="images", default="static/coins/images/default_coin_image.jpeg")


    def __unicode__(self):
        return self.title
    
    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date < now

class coin_in_corpus(models.Model):
    corpus            = models.ForeignKey(Corpus, default="tester")
    coin              = models.ForeignKey(Coin, default="tester")
