# Generated by Django 2.2.3 on 2019-07-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('roll', models.CharField(blank=True, max_length=64, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('areas_of_interest', models.TextField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ECE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('roll', models.CharField(blank=True, max_length=64, null=True)),
                ('areas_of_interest', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]