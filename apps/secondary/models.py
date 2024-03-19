from django.db import models

# Create your models here.

class InfoUser(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name = "Имя")
    
    description = models.CharField(
        max_length=255,
        verbose_name = "Описание" 
    )
    
    age = models.IntegerField(
        verbose_name = "Ваш возраст"
    )
    
    email = models.EmailField(
        verbose_name = "Ваша эл.почта"
    )
    
    country = models.CharField( 
        max_length=50,
        verbose_name = "Ваша страна"
    )
    youtube = models.URLField(
        verbose_name = 'YouTube'
    )
    
    instagram = models.URLField(
        verbose_name = 'Instagram'
    )
    
    whatsapp = models.URLField(
        verbose_name = 'Whatsapp'
    )
    
    telegram = models.URLField(
        verbose_name = 'Telegram'
    )
    
    facebook = models.URLField(
    verbose_name = 'Facebook'
    )
    
    class Meta:
        verbose_name = "Информация о пользователя"
        verbose_name_plural = "Информация о пользователей"
        
class Resume(models.Model):
    full_name = models.CharField(
        max_length = 50,
        verbose_name = "Ваше полное имя"
    )
    
    location = models.CharField(
        max_length=255,
        verbose_name = "Локация"
    )
    
    number = models.CharField(
        max_length=50,
        verbose_name = "Ваш номер телефона"
    )
    
    email = models.EmailField(
        max_length=254,
        verbose_name= "Ваша эл.почта")
    
    class Meta:
        verbose_name_plural = "Резюме"
        
class Experience(models.Model):
        experience1 = models.CharField(
            max_length=255,
            verbose_name = "Кем вы работали"
        )
        description = models.CharField(
            max_length=255,
            verbose_name="Описание"
        )
        
        work_company = models.CharField(
            max_length=255,
            verbose_name="В какой компании вы работали"
        )
        
        class Meta:
            verbose_name_plural = "Опыт работы"
            
class Blogs(models.Model):
    blog1 = models.ImageField(
        verbose_name="Ваш первый блог"
        
    )
    data1 = models.DateField(verbose_name="Дата")
    
    description1 = models.CharField(
        max_length=255,
        verbose_name="Описание"
    )
    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        
class Portfolio(models.Model):
    name = models.CharField(
        max_length=55,
        verbose_name="Имя"
    )
    
    about = models.CharField(
        max_length=255,
        verbose_name="О вас"
    )
    
    email = models.CharField(
        max_length=50,
        verbose_name="Эл.почта"
    )
    
    class Meta:
        verbose_name_plural = "Портфолио"