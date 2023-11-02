# Generated by Django 4.2.7 on 2023-11-02 07:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0008_delete_groups_delete_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('ID_Groups', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Course_number', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('Group_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('ID_subjects', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Group_number', models.CharField(max_length=50)),
            ],
        ),
    ]