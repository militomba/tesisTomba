# Generated by Django 3.2.12 on 2023-06-07 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_alter_datosusuarios_centrocomercial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scanner',
            fields=[
                ('datosusuarios_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.datosusuarios')),
                ('token', models.CharField(max_length=500)),
            ],
            bases=('usuarios.datosusuarios',),
        ),
    ]
