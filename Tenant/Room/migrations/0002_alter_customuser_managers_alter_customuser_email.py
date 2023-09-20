# Generated by Django 4.2.1 on 2023-09-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]