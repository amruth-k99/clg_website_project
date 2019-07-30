# Generated by Django 2.2.3 on 2019-07-29 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cse',
            options={'verbose_name_plural': 'CSE'},
        ),
        migrations.AlterModelOptions(
            name='ece',
            options={'verbose_name_plural': 'ECE'},
        ),
        migrations.AddField(
            model_name='cse',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='ece',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]