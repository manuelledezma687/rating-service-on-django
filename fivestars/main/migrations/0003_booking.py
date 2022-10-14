# Generated by Django 4.1.2 on 2022-10-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up', models.CharField(max_length=50)),
                ('destiny', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('flight', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('date_time', models.CharField(max_length=50)),
                ('payment_method', models.CharField(max_length=12)),
                ('type_of_travel', models.CharField(max_length=12)),
                ('observations', models.CharField(max_length=100)),
                ('passengers', models.IntegerField()),
            ],
        ),
    ]
