# Generated by Django 4.1 on 2022-11-17 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('phnNo', models.CharField(max_length=100, unique=True)),
                ('gender', models.CharField(default='none', max_length=100)),
                ('paymentMode', models.CharField(max_length=100)),
                ('regDate', models.DateField(auto_now=True)),
                ('story', models.CharField(max_length=100)),
                ('checkIn', models.CharField(max_length=10)),
            ],
        ),
    ]
