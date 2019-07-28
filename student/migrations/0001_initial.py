# Generated by Django 2.2.3 on 2019-07-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('html', models.TextField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=64, null=True)),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]