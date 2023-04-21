# Generated by Django 3.2.12 on 2023-04-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codigoQR', '0002_auto_20230420_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codigoqr',
            name='titulo',
        ),
        migrations.AddField(
            model_name='codigoqr',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='qrCode'),
        ),
        migrations.AlterField(
            model_name='codigoqr',
            name='contenido',
            field=models.CharField(max_length=200),
        ),
    ]
