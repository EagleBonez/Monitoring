# Generated by Django 2.2.9 on 2020-04-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning_approvals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planningapp',
            name='current_status',
            field=models.CharField(default='Extant', help_text='Current status of application', max_length=30),
        ),
    ]