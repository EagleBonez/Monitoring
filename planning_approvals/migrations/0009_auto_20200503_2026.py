# Generated by Django 2.2.9 on 2020-05-03 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planning_approvals', '0008_auto_20200503_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planningapp',
            old_name='year_five',
            new_name='year_01',
        ),
        migrations.RenameField(
            model_name='planningapp',
            old_name='year_four',
            new_name='year_02',
        ),
        migrations.RenameField(
            model_name='planningapp',
            old_name='year_one',
            new_name='year_03',
        ),
        migrations.RenameField(
            model_name='planningapp',
            old_name='year_three',
            new_name='year_04',
        ),
        migrations.RenameField(
            model_name='planningapp',
            old_name='year_two',
            new_name='year_05',
        ),
    ]
