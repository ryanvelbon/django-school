# Generated by Django 2.0.7 on 2018-07-14 19:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180714_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='mob_parent',
            field=models.CharField(blank=True, max_length=8, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\d{8}$')], verbose_name="Parent's Mobile"),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mob_student',
            field=models.CharField(blank=True, max_length=8, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\d{8}$')], verbose_name="Student's Mobile"),
        ),
    ]