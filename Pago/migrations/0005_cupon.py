# Generated by Django 3.0.1 on 2023-03-07 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pago', '0004_delete_cupon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
            ],
        ),
    ]