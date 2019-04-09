# Generated by Django 2.2 on 2019-04-08 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190408_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='postactivity',
            name='members',
            field=models.ForeignKey(default='empty', on_delete=django.db.models.deletion.CASCADE, to='api.Member'),
        ),
        migrations.AddField(
            model_name='postactivity',
            name='status',
            field=models.CharField(choices=[('O', 'Owner'), ('C', 'Contributor'), ('R', 'Reader')], default='O', max_length=1),
        ),
    ]
