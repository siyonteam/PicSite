# Generated by Django 3.1.7 on 2021-06-19 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_auto_20210617_0604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='craeted',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='picture',
            old_name='craeted',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_sub_cat',
        ),
        migrations.RemoveField(
            model_name='category',
            name='up_cat',
        ),
    ]
