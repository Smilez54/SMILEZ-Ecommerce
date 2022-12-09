# Generated by Django 4.1 on 2022-08-30 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smilez', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='fname',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]