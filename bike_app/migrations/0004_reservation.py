# Generated by Django 4.1.7 on 2023-06-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_app', '0003_worker_useraccount_worker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('Reservation_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Reservation_DateRequest', models.CharField(max_length=30)),
                ('Reservation_DateEnd', models.CharField(max_length=30)),
                ('Reservation_Bike', models.CharField(choices=[('bike1', 'Bike 1'), ('bike2', 'Bike 2'), ('bike3', 'Bike 3')], max_length=20)),
                ('Reservation_status', models.CharField(max_length=20)),
                ('Reservation_Number', models.CharField(max_length=5)),
            ],
        ),
    ]
