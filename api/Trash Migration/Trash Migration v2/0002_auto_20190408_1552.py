# Generated by Django 2.2 on 2019-04-08 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChildList',
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]
