# Generated by Django 2.2.17 on 2021-01-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edx_proctoring', '0012_proctoredexamstudentattempt_time_remaining_seconds'),
    ]

    operations = [
        migrations.AddField(
            model_name='proctoredexamsoftwaresecurereview',
            name='is_attempt_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='proctoredexamsoftwaresecurereviewhistory',
            name='is_attempt_active',
            field=models.BooleanField(default=True),
        ),
    ]