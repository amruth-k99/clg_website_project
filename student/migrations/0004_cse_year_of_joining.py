# Generated by Django 2.2.3 on 2019-07-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190728_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='cse',
            name='year_of_joining',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]
