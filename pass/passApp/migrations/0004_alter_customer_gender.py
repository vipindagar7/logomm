# Generated by Django 4.1 on 2022-11-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passApp', '0003_alter_customer_phnno_alter_customer_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], default='NONE', max_length=128),
        ),
    ]
