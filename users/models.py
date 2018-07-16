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

    GENDER_CHOICES = (
        ('boys', 'boys'),
        ('girls', 'girls'),
        ('mixed', 'mixed'),
    )

    name = models.CharField(max_length=80)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True)
    type = models.CharField(
        max_length = 20,
        choices=TYPE_OF_SCHOOL_CHOICES,
    )
    gender = models.CharField(
        max_length = 10,
        choices = GENDER_CHOICES,
        default = 'mixed',
    )

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):

    # override User model's first_name and last_name fields to make them required
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=False)

    phone_regex = RegexValidator(regex=r'^\d{8}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    mob_parent = models.CharField(
        validators=[phone_regex],
        max_length=8,
        blank=True,
        verbose_name="Parent's Mobile",
    )

    mob_student = models.CharField(
        validators=[phone_regex],
        max_length=8,
        blank=True,
        verbose_name="Student's Mobile",
    )

    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not (self.mob_parent or self.mob_student):
            # 1. Encapsulate the condition in a validator function __validate_at_least_one_mob()
            # 2. raise validation error? or maybe make a clean() method?
            return
        else:
            super().save(*args, **kwargs)
    
