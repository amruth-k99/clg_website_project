# Generated by Django 2.2.3 on 2019-07-24 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subpages', '0005_auto_20190723_1716'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubPageContent',
            new_name='Content_with_1_image',
        ),
        migrations.RenameModel(
            old_name='SubPageContent2',
            new_name='Content_with_2_image',
        ),
        migrations.RenameModel(
            old_name='SubPageContent3',
            new_name='Content_with_3_image',
        ),
    ]