from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(
        max_length = 255, verbose_name = 'Имя')
    lastname = models.CharField(
        max_length = 255, verbose_name = 'Фамилие')
    phone_number = models.CharField(
        max_length = 25, verbose_name = 'Номер')
    job = models.CharField(
        max_length = 255, verbose_name = 'Ваша работа')
    image = models.ImageField(
        upload_to='UserInfo', verbose_name= 'Фото')
    description = models.TextField(
        verbose_name = 'Описание')
    age = models.IntegerField(
        verbose_name = 'Возраст')
    email = models.EmailField(
        verbose_name = 'Эл.почта')
    address = models.CharField(
        max_length = 255, verbose_name = 'Адрес')
    location = models.CharField(
        max_length = 255, verbose_name = 'Локация')
    twitter = models.URLField(
        verbose_name = 'Twitter')
    facebook = models.URLField(
        verbose_name = 'Facebook')
    linkedin = models.URLField(
        verbose_name = 'Linkedin')
    github = models.URLField(
        verbose_name = 'Github')
    instagram = models.URLField(
        verbose_name = 'Instagram')

    def __str__(self) -> str:
        return f"{self.name} {self.lastname}"

    class Meta:
        verbose_name_plural = 'Aдминистратор пользователей'

class Service(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Сервисы'

class Experience(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Название')
    place = models.CharField(max_length = 30, verbose_name = 'Место')
    year = models.CharField(max_length = 255, verbose_name = 'Год')
    subtitle = models.CharField(max_length = 255, verbose_name = 'Субтитры')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "Опыты"

class Educations(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Название')
    place = models.CharField(max_length = 30, verbose_name = 'Место')
    year = models.CharField(max_length = 255, verbose_name = 'Год')
    subtitle = models.CharField(max_length = 255, verbose_name = 'Подзаголовок')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "Образовние"

class Skills(models.Model):
    id = models.IntegerField(primary_key = True, verbose_name = 'ID')
    lang = models.CharField(max_length = 50, verbose_name = 'Язык')
    def __str__(self) -> str:
        return self.lang
    
    class Meta:
        verbose_name_plural = "Знания"

class Office(models.Model):
    id = models.IntegerField(primary_key = True, verbose_name = 'ID')
    description = models.TextField(verbose_name = 'Описание')
    image = models.URLField(verbose_name='Видео')

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name_plural = "Oффисы"

class Portfolio(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    image = models.ImageField(upload_to='Portfolio', verbose_name='Фото')
    choosing = models.CharField(max_length = 50, verbose_name = 'Фото Дизайн Брэнд')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "Портфолио"

class Blog(models.Model):
    image = models.ImageField(upload_to='Portfolio', verbose_name='Фото')
    data = models.DateField(verbose_name = 'Date')
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "Блоги"