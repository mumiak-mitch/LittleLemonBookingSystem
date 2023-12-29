# Generated by Django 5.0 on 2023-12-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('reservation_date', models.DateField()),
                ('reservation_slot', models.CharField(max_length=100)),
            ],
        ),
    ]
