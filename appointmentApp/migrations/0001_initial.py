# Generated by Django 4.1.5 on 2023-01-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('request', models.TextField(blank=True)),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
    ]
