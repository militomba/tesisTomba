# Generated by Django 3.2.12 on 2023-05-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamiento', '0002_alter_centrocomercialespecifico_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centrocomercialespecifico',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
