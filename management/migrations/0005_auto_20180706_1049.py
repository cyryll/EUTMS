# Generated by Django 2.0.6 on 2018-07-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20180706_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='Request_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='request ID'),
        ),
    ]
