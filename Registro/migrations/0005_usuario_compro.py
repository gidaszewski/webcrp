# Generated by Django 3.0.1 on 2023-04-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0004_auto_20230327_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='compro',
            field=models.BooleanField(default=False),
        ),
    ]
