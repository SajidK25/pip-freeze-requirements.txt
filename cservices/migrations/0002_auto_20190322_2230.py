# Generated by Django 2.1.7 on 2019-03-22 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cservices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='education',
            new_name='current_education',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='password',
            new_name='desired_interest',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='username',
            new_name='desired_major',
        ),
    ]