# Generated by Django 4.1.5 on 2023-02-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_remove_predictedresult_user_id_predictedresult_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictedresult',
            name='id',
        ),
        migrations.AddField(
            model_name='predictedresult',
            name='user_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]