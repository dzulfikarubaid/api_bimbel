# Generated by Django 4.2.1 on 2023-05-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='nama_cabang',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
