# Generated by Django 2.0.6 on 2018-09-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_marks_questions_register_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.TextField(max_length=300),
        ),
    ]