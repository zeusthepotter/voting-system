# Generated by Django 2.0.3 on 2018-04-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_name', models.CharField(max_length=30)),
                ('voter_roll', models.IntegerField(max_length=10)),
                ('voter_userid', models.CharField(max_length=30)),
                ('voter_email', models.CharField(max_length=50)),
                ('voter_password', models.CharField(max_length=15)),
            ],
        ),
    ]