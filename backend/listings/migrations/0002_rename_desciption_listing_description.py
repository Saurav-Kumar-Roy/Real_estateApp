# Generated by Django 4.2.3 on 2023-07-29 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='desciption',
            new_name='description',
        ),
    ]