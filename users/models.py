from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class Locality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'localities'




class School(models.Model):

    TYPE_OF_SCHOOL_CHOICES = (
        ('public', 'public school'),
        ('private', 'private school'),
        ('church', 'Church school'),
    )

    name = models.CharField(max_length=80)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True)
    type = models.CharField(
        max_length = 20,
        choices=TYPE_OF_SCHOOL_CHOICES,
    )

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):

    phone_regex = RegexValidator(regex=r'^\d{8}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    mob_student = models.CharField(
        validators=[phone_regex],
        max_length=8,
        blank=True
    )

    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True)