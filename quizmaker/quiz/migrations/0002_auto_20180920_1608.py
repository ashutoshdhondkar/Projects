# Generated by Django 2.0.6 on 2018-09-20 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Marks',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='Register_Users',
        ),
    ]
