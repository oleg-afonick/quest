# Generated by Django 4.2.7 on 2023-11-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0009_groups_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='ID_Groups',
        ),
        migrations.AlterField(
            model_name='groups',
            name='Group_number',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
