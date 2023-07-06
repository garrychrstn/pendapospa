# Generated by Django 4.1.7 on 2023-06-23 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.IntegerField()),
                ('nama', models.CharField(max_length=40)),
                ('tgl', models.DateField()),
                ('kelamin', models.CharField(max_length=10)),
                ('namaibu', models.CharField(max_length=40)),
                ('nikibu', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Posyandu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ke', models.IntegerField()),
                ('tb', models.IntegerField()),
                ('bb', models.IntegerField()),
                ('ll', models.IntegerField()),
                ('lk', models.IntegerField()),
                ('ket', models.CharField(max_length=20)),
                ('nik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profil')),
            ],
        ),
    ]