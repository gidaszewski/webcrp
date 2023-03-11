# Generated by Django 3.0.1 on 2023-03-10 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0008_auto_20230310_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='categoria',
            field=models.CharField(choices=[('', 'Seleccione una categoria'), ('1', 'Edad: 15-20 años'), ('2', 'Edad: 20-25 años'), ('3', 'Edad: 25-30 años'), ('4', 'Edad: 30-35 años'), ('5', 'Edad: 35-40 años'), ('6', 'Edad: 40-45 años'), ('7', 'Edad: 45-50 años'), ('8', 'Edad: 50-55 años'), ('9', 'Edad: 55-60 años'), ('10', 'Edad: 60-65 años'), ('11', 'Edad: +70 años')], default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('', 'Seleccione su genero'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otros', 'Otros')], default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='talle_de_remera',
            field=models.CharField(choices=[('', 'Seleccione un talle de remera'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.BigIntegerField(null=True),
        ),
    ]
