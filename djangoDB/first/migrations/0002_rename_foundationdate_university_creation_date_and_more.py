# Generated by Django 4.2.6 on 2023-11-13 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='foundationDate',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='fullTitle',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='shortTitle',
            new_name='short_name',
        ),
        migrations.AlterModelTable(
            name='university',
            table='university',
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('enrollment_year', models.DateField(verbose_name='Дата выпуска')),
                ('university_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.university')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'db_table': 'student',
            },
        ),
    ]