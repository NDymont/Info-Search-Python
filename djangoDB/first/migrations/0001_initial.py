# Generated by Django 4.2.6 on 2023-11-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullTitle', models.CharField(max_length=100, verbose_name='Полное название')),
                ('shortTitle', models.CharField(max_length=10, verbose_name='Сокращенное название')),
                ('foundationDate', models.DateField(verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Университет',
                'verbose_name_plural': 'Университеты',
            },
        ),
    ]
