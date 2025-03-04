# Generated by Django 4.1.5 on 2023-02-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointmentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualCounsellor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('main', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=256)),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]
