# Generated by Django 5.1.6 on 2025-02-17 20:01

import django.utils.timezone
import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=225, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=225, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=225, null=True)),
                ('last_name', models.CharField(blank=True, max_length=225, null=True)),
                ('date_of_birth', models.DateField(blank=True, help_text='YYYY-MM-DD', null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, null=True)),
                ('identity_document_type', models.CharField(blank=True, choices=[('Voter ID', 'Voter ID'), ('Passport', 'Passport'), ('Citizenship Number', 'Citizenship Number')], max_length=225, null=True)),
                ('identity_document_number', models.CharField(blank=True, max_length=225, null=True)),
                ('photo', models.ImageField(null=True, upload_to='profileImage/')),
                ('get_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
    ]
