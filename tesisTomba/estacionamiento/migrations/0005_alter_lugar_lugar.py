# Generated by Django 3.2.12 on 2023-05-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamiento', '0004_alter_centrocomercialespecifico_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='lugar',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
