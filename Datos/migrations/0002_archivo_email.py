# Generated by Django 3.0.1 on 2023-04-04 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]