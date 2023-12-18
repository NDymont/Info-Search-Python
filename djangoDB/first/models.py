from django.db import models


# Create your models here.
class University(models.Model):
    # id = models.IntegerField('id')
    full_name = models.CharField('Полное название', max_length=100)
    short_name = models.CharField('Сокращенное название', max_length=10)
    creation_date = models.DateField('Дата создания')

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return f'/universities'

    class Meta:
        verbose_name = "Университет"
        verbose_name_plural = "Университеты"
        db_table = "university"


class Student(models.Model):
    # id = models.IntegerField('id')
    full_name = models.CharField('ФИО', max_length=100)
    university = models.ForeignKey(University,  on_delete=models.CASCADE)
    birth_date = models.DateField('Дата рождения')
    enrollment_year = models.IntegerField('Год выпуска')

    def str(self):
        return self.full_name

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return f'/students'

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        db_table = "student"
