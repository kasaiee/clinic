from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from webpush import send_user_notification
from django.contrib.auth import get_user_model
User = get_user_model()


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    accepted = models.BooleanField(default=False)
    name = models.CharField(max_length=70)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20)
    speciality = models.ForeignKey('Speciality', on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)

    def __str__(self):
        # return '%s at %s' % (self.name, self.date)
        return f'{self.name} at {self.date}'


@receiver(pre_save, sender=Appointment)
def send_web_push(sender, instance, *args, **kwargs):
    native_obj_pk = instance.id
    if native_obj_pk:
        native_obj = sender.objects.get(pk=native_obj_pk)
        if native_obj.accepted != instance.accepted:
            canceled = native_obj.accepted and not instance.accepted
            payload = {
                "head": f"Dear {instance.name}!",
                "icon": "http://127.0.0.1:8000/static/base/images/logo.png",
                "body": f'''
                    Your appointment at
                    {instance.date} by {instance.doctor} ({instance.speciality}),
                    {"calceled" if canceled else "accepted"}!
                '''
            }
            send_user_notification(user=instance.user, payload=payload, ttl=1000)
    # instance.slug = slugify(instance.title)

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
        

class Subscriber(models.Model):
    email = models.EmailField('Your email', max_length=100, null=True)

    def __str__(self):
        return self.email
        