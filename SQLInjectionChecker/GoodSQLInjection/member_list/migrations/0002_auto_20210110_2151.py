# Generated by Django 3.1.5 on 2021-01-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(),
        ),
    ]
