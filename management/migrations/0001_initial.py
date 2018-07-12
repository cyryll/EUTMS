# Generated by Django 2.0.6 on 2018-07-05 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('Staff_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.Staff')),
                ('Availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Mechanics',
            fields=[
                ('Staff_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.Staff')),
                ('Availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('Request_id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='request ID')),
                ('DeptRequesting', models.CharField(max_length=100)),
                ('Reason', models.CharField(max_length=100)),
                ('Travel_date', models.DateTimeField()),
                ('Return_date', models.DateTimeField()),
                ('Destination', models.CharField(max_length=40)),
                ('Travellers_desc', models.SmallIntegerField()),
                ('Capacity', models.IntegerField()),
                ('Cofirm_status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SpareParts',
            fields=[
                ('SparePart_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Spare part ID')),
                ('Amount', models.IntegerField(verbose_name='Quantity')),
                ('Name', models.CharField(max_length=100, verbose_name='Name')),
                ('Cost', models.IntegerField(verbose_name='Cost')),
                ('Description', models.CharField(max_length=255, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('Number_plate', models.CharField(max_length=7, primary_key=True, serialize=False, unique=True, verbose_name='Lisence Plate')),
                ('Vehicle_type', models.CharField(max_length=15, verbose_name='Vehicle type')),
                ('Engine_capacity', models.CharField(max_length=10, verbose_name='Engine Capacity')),
                ('Capacity', models.IntegerField(verbose_name='Vehicle Capacity')),
                ('Driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='management.Drivers')),
                ('Mechanic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mechanic', to='management.Mechanics')),
            ],
        ),
        migrations.CreateModel(
            name='BusAllocation',
            fields=[
                ('Request_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='management.Requests')),
                ('Driver_fee', models.IntegerField()),
                ('Fuel_money', models.IntegerField()),
                ('Estimated_distance', models.IntegerField()),
                ('Driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Drivers')),
                ('Vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Vehicles')),
            ],
        ),
        migrations.AddField(
            model_name='requests',
            name='User_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]