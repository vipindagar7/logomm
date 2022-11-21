# Generated by Django 4.1 on 2022-11-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passApp', '0004_alter_customer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='checkIn',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='NO', max_length=128),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='NONE', max_length=128),
        ),
    ]