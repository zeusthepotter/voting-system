# Generated by Django 2.0.3 on 2018-04-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_voter_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='voter_userid',
        ),
        migrations.AlterField(
            model_name='voter',
            name='voter_roll',
            field=models.CharField(max_length=10),
        ),
    ]
