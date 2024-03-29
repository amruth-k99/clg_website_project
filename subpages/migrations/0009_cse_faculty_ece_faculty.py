# Generated by Django 2.2.3 on 2019-07-26 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subpages', '0008_photo_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSE_Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ECE_Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]
