from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import pytils.translit
# Create your models here.


class Organization(models.Model):
    title = models.CharField(verbose_name='Название', max_length=500, null=False, blank=False)
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['title']
        verbose_name = "Организация"
        verbose_name_plural = "Организации"


class CollegialBody(models.Model):
    title = models.CharField(verbose_name='Название', max_length=500, null=False, blank=False)
    organization = models.ForeignKey(to="structure.Organization", related_name='collegial_bodies', on_delete=models.CASCADE, null=False, blank=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['title']
        verbose_name = "Коллегиальный орган"
        verbose_name_plural = "Коллегиальные органы"


class AdministrativeBody(models.Model):
    title = models.CharField(verbose_name='Название', max_length=500, null=False, blank=False)
    collegial_body = models.ForeignKey(to="structure.CollegialBody", related_name="administrative_bodies",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Административный орган"
        verbose_name_plural = "Административные органы"

class Director(models.Model):
    title = models.CharField(verbose_name='Название', max_length=500, null=False, blank=False)
    user_code = models.CharField(verbose_name="Код", max_length=20, null=True, blank=False)
    subdivision = models.ForeignKey(to='structure.Subdivision', related_name='directors',on_delete=models.CASCADE, null=True, blank=True)
    administrative_body = models.ForeignKey(to="structure.AdministrativeBody", related_name="directors", on_delete=models.CASCADE, null=True, blank=True)
    collegial_body = models.ForeignKey(to="structure.CollegialBody", related_name="directors", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководители"


class Subdivision(models.Model):
    title = models.CharField(verbose_name='Название', max_length=500, null=False, blank=False)
    director = models.ForeignKey(to="structure.Director", related_name='subdivisions', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"
        
class Position(models.Model):
    title = models.CharField(verbose_name='Название', max_length=500, null=False, blank=False)
    user_code = models.CharField(verbose_name="Код", max_length=20, null=True, blank=False)
    subdivision = models.ForeignKey(to="structure.Subdivision", related_name='positions', on_delete=models.CASCADE, null=True, blank=True)
    administrative_body = models.ForeignKey(to="structure.AdministrativeBody", related_name='positions', on_delete=models.CASCADE, null=True, blank=True)
    collegial_body = models.ForeignKey(to="structure.CollegialBody", related_name='positions', on_delete=models.CASCADE, null=True, blank=True)
    director = models.ForeignKey(to="structure.Director", related_name='positions', on_delete=models.CASCADE, null=True,blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        
        
def user_photo_path(instance, filename):
    username = instance.username
    return f"persons/{username}/{filename}"

class Person(AbstractUser):
    userPhoto = models.ImageField(verbose_name="Фото пользователя",upload_to=user_photo_path, null=True, blank=True)
    fullname = models.CharField(verbose_name='ФИО', max_length=500, null=False, blank=False)
    position = models.ManyToManyField(to="structure.Position",   related_name ="persons", null=True,blank=True)
    director = models.OneToOneField(to="structure.Director", related_name="person", on_delete=models.CASCADE, null=True,blank=True)
    stavka = models.PositiveIntegerField(verbose_name="Ставка", null=True, blank=False)
    
    
    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = pytils.translit.translify(self.fullname)
        if not self.userPhoto:
            self.userPhoto = f'img/avatar.png'
            
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['username']
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"   
        

class Task(models.Model):        
    person = models.ForeignKey(to="structure.Person", related_name='tasks', on_delete=models.CASCADE, null=False, blank=False)
    date_start = models.DateTimeField(verbose_name="Дата создания",null=False,blank=False,default=timezone.now)
    date_finish = models.DateTimeField(verbose_name="Дата окончания",null=False,blank=False)
    description = models.TextField(verbose_name='Описание задачи', max_length=1000, null=False, blank=False)

    class Meta:
        ordering = ['date_start']
        verbose_name = "Задача"
        verbose_name_plural = "Задачи" 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
