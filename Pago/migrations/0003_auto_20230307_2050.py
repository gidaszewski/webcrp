# Generated by Django 3.0.1 on 2023-03-07 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pago', '0002_auto_20230307_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cupon',
            old_name='descuentos',
            new_name='descuento',
        ),
    ]
