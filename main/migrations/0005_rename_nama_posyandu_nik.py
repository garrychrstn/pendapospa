# Generated by Django 4.1.7 on 2023-06-23 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_nik_posyandu_nama'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posyandu',
            old_name='nama',
            new_name='nik',
        ),
    ]