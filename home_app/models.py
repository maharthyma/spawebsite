from django.db import models


# Create your models here.
class ContactUs(models.Model):
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=100)
    Location = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Contact Us'


class portfolio(models.Model):
    Name = models.CharField(max_length=100)
    About = models.TextField()
    Picture = models.FileField(upload_to='Portfolio')

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = 'Portfolio'


class Package(models.Model):
    Name = models.CharField(max_length=100)
    Offer1 = models.CharField(max_length=100)
    Offer2 = models.CharField(max_length=100)
    Offer3 = models.CharField(max_length=100)
    Offer4 = models.CharField(max_length=100)
    Offer5 = models.CharField(max_length=100)
    Price = models.IntegerField()

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = 'Package'
