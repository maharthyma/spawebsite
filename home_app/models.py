from django.db import models


# Create your models here.
class ContactUs(models.Model):
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=100)
    Location = models.TextField()
    Facebook = models.URLField()
    Twitter = models.URLField()
    Instagram = models.URLField()
    Youtube = models.URLField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Contact Us'


class portfolio(models.Model):
    Name = models.CharField(max_length=100)
    About = models.TextField()
    Picture = models.FileField(upload_to='Portfolio/')

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


class Carousel(models.Model):
    Heading1 = models.CharField(max_length=100)
    Heading2 = models.CharField(max_length=100)
    Paragraph = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Heading1)

    class Meta:
        verbose_name_plural = 'Carousel'


class Statistics(models.Model):
    Name = models.CharField(max_length=100)
    Number = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = 'Statistics'


class Review(models.Model):
    Name = models.CharField(max_length=100)
    Service = models.CharField(max_length=100)
    Review = models.TextField(max_length=100)
    Image = models.FileField(upload_to='Review/')

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = 'Review'


class Reservation(models.Model):
    Client_Name = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=100)
    Email = models.EmailField()
    Time = models.CharField(max_length=100)
    Message=models.TextField()
    Package = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Client_Name)

    class Meta:
        verbose_name_plural = 'Reservation'


class About(models.Model):
    AboutText = models.TextField()
    AboutPoint1 = models.CharField(max_length=100)
    AboutPoint2 = models.CharField(max_length=100)
    AboutPoint3 = models.CharField(max_length=100)
    Picture = models.FileField(upload_to='Team/')

    def __str__(self):
        return str(self.AboutText)

    class Meta:
        verbose_name_plural = 'About'


class Team(models.Model):
    Name = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    About = models.CharField(max_length=100)
    Picture = models.FileField(upload_to='Team/')
    Twitter = models.URLField()
    Instagram = models.URLField()
    Facebook = models.URLField()

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = 'Team'


class About_2(models.Model):
    About_Heading = models.CharField(max_length=100)
    About = models.CharField(max_length=100)

    def __str__(self):
        return str(self.About_Heading)

    class Meta:
        verbose_name_plural = 'About (for Home)'
