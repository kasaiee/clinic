from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20)
    speciality = models.ForeignKey('Speciality', on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)


class Speciality(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'
    
    def __str__(self):
        return self.name


class Doctor(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    speciality = models.ManyToManyField(Speciality)

    def __str__(self):
        return self.fname + ' ' + self.lname


class Service(models.Model):
    name = models.CharField(max_length=40, null=True)
    description = models.TextField(null=True)
    price = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name