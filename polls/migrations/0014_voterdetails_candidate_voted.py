# Generated by Django 2.0.3 on 2018-04-13 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_remove_voterdetails_candidate_voted'),
    ]

    operations = [
        migrations.AddField(
            model_name='voterdetails',
            name='candidate_voted',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Candidate'),
        ),
    ]