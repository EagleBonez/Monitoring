# Generated by Django 2.2.9 on 2020-04-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning_approvals', '0003_auto_20200414_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='address',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
