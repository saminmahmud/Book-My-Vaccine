# Generated by Django 5.1.6 on 2025-02-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Vaccine Name')),
                ('description', models.TextField()),
                ('number_of_doses', models.IntegerField(default=1)),
                ('interval', models.IntegerField(default=0, help_text='Please provide interval in days')),
                ('storage_temperature', models.IntegerField(blank=True, help_text='Please provide storage temperature in Celsius', null=True)),
                ('minimum_age', models.IntegerField(default=0)),
            ],
        ),
    ]
