# Generated by Django 2.0.3 on 2018-04-19 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laddr_site', '0003_auto_20180418_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
