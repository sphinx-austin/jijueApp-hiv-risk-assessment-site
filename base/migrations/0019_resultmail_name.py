# Generated by Django 4.1.5 on 2023-02-09 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_delete_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultmail',
            name='name',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
