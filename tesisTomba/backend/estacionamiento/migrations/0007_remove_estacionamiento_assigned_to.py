# Generated by Django 3.2.12 on 2023-04-21 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamiento', '0006_alter_estacionamiento_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estacionamiento',
            name='assigned_to',
        ),
    ]