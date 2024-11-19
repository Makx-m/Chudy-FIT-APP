from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.IntegerField(default=130)
    sex = models.IntegerField(default=0)
    age = models.IntegerField(default=18)
    image = models.ImageField(upload_to='person_media', blank=True, null=True)
    activePerDay = models.IntegerField(default=0)

    def __str__(self):
        return "{}, waga: {}, wzrost: {}".format(self.name, self.weight, self.height)

    def is_male(self):
        return self.sex == 2

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Uczestnicy'

