# Generated by Django 4.1.7 on 2023-06-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_nama_posyandu_nik'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='nikibu',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='profil',
            name='tempat',
            field=models.CharField(default='Sumberejo', max_length=30),
        ),
    ]