from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length = 255, verbose_name = 'user name')
    lastname = models.CharField(max_length = 255, verbose_name = 'user surname')
    phone_number = models.CharField(max_length = 25, verbose_name = 'user phone number')
    job = models.CharField(max_length = 255, verbose_name = 'user job')
    image = models.ImageField(upload_to='UserInfo', verbose_name= 'user image')
    description = models.TextField(verbose_name = 'user description')
    age = models.IntegerField(verbose_name = 'user age')
    email = models.EmailField(verbose_name = 'user email')
    address = models.CharField(max_length = 255, verbose_name = 'user address')
    location = models.CharField(max_length = 255, verbose_name = 'user location')
    twitter = models.URLField(verbose_name = 'Twitter')
    facebook = models.URLField(verbose_name = 'Facebook')
    linkedin = models.URLField(verbose_name = 'Linkedin')
    github = models.URLField(verbose_name = 'Github')
    instagram = models.URLField(verbose_name = 'Instagram')

    def __str__(self) -> str:
        return f"{self.name} {self.lastname}"

    class Meta:
        verbose_name = 'User admin'
        verbose_name_plural = 'Users admin'

class Service(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Title')
    description = models.TextField(verbose_name = 'Description')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class Testimonials(models.Model):
    image = models.ImageField(upload_to= 'Testimonialers', verbose_name= 'Testimonialer image')
    fullname = models.CharField(max_length = 255, verbose_name= 'Testimonialer fullname')
    job = models.CharField(max_length = 70, verbose_name= 'Testimonialer job')
    testimonial = models.TextField(verbose_name = 'Testimonialer testimonial')

    def __str__(self) -> str:
        return self.fullname

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

class Experience(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Title')
    place = models.CharField(max_length = 30, verbose_name = 'Place')
    year = models.CharField(max_length = 255, verbose_name = 'Year')
    subtitle = models.CharField(max_length = 255, verbose_name = 'SubTitle')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

class Educations(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Title')
    place = models.CharField(max_length = 30, verbose_name = 'Place')
    year = models.CharField(max_length = 255, verbose_name = 'Year')
    subtitle = models.CharField(max_length = 255, verbose_name = 'SubTitle')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"

class Skills(models.Model):
    id = models.IntegerField(primary_key = True, verbose_name = 'ID')
    lang = models.CharField(max_length = 50, verbose_name = 'Language')
    percent = models.IntegerField(verbose_name = 'Percent')

    def __str__(self) -> str:
        return self.lang
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

class Office(models.Model):
    id = models.IntegerField(primary_key = True, verbose_name = 'ID')
    description = models.TextField(verbose_name = 'Description')
    image = models.URLField(verbose_name='Video')

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = "Office"
        verbose_name_plural = "Offices"

class Portfolio(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Title')
    image = models.ImageField(upload_to='Portfolio', verbose_name='Image')
    choosing = models.CharField(max_length = 50, verbose_name = 'photos/design/brand')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolioes"

class Blog(models.Model):
    image = models.ImageField(upload_to='Portfolio', verbose_name='Image')
    data = models.DateField(verbose_name = 'Date')
    title = models.CharField(max_length = 150, verbose_name = 'Title')
    description = models.TextField(verbose_name = 'Description')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"