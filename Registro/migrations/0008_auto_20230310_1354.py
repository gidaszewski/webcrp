# Generated by Django 3.0.1 on 2023-03-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0007_auto_20230310_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
