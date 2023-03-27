# Generated by Django 4.1.5 on 2023-03-27 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("admin_id", models.CharField(max_length=20, unique=True)),
                ("admin_email", models.CharField(max_length=20)),
                ("admin_password", models.CharField(max_length=20)),
                ("admin_login", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="BikeInfo",
            fields=[
                (
                    "BikeCode",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("BikeName", models.CharField(max_length=20)),
                ("BikeType", models.CharField(max_length=20)),
                ("Descriptions", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Complaint",
            fields=[
                (
                    "complaint_id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("Descriptions", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("surname", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=128)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "Reservation_id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("Reservation_DateRequest", models.CharField(max_length=30)),
                ("Reservation_DateEnd", models.CharField(max_length=30)),
                ("Reservation_Bike", models.CharField(max_length=20)),
                ("Reservation_status", models.CharField(max_length=20)),
            ],
        ),
    ]