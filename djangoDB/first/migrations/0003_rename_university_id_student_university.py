# Generated by Django 4.2.6 on 2023-11-13 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_rename_foundationdate_university_creation_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='university_id',
            new_name='university',
        ),
    ]
