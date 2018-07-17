from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

from django.core.exceptions import ValidationError

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

    phone_regex = RegexValidator(regex=r'^\d{8}$', message="Phone number must be exactly 8 digits long.")

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

    def clean(self):
        """Django's clean() method should be used to provide custom model validation, and to modify attributes on your model if desired. For instance, you could use it to automatically provide a value for a field, or to do validation that requires access to more than a single field."""

        if not (self.mob_parent or self.mob_student):
            raise ValidationError("Please enter at least one mobile number.")
        self.username = self.generate_username()

    # def save(self, *args, **kwargs):
    #     # do some custom shit
    #     super().save(*args, **kwargs)

    def generate_username(self):
        val = "{0}{1}".format(self.first_name[0],self.last_name).lower()
        x=0
        while True:
            if x == 0 and CustomUser.objects.filter(username=val).count() == 0:
                return val
            else:
                new_val = "{0}{1}".format(val,x)
                if CustomUser.objects.filter(username=new_val).count() == 0:
                    return new_val
                x += 1
                if x > 1000000:
                    raise Exception("Too many users have same name. Cannot generate username.")
