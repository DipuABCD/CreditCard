# Generated by Django 3.2.18 on 2023-03-28 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcardapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='creditcardapply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 28, 2, 4, 33, 533774))),
                ('fname', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('mothername', models.CharField(max_length=150)),
                ('jobdesignation', models.CharField(max_length=150)),
                ('sallary', models.BigIntegerField()),
                ('birthdate', models.DateField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.BigIntegerField()),
                ('aadharcard', models.FileField(upload_to='AadharCard')),
                ('pancard', models.FileField(upload_to='PanCard')),
                ('userimages', models.FileField(upload_to='User_Images')),
                ('bankstatement', models.FileField(upload_to='BankStatement')),
                ('sllaryslip', models.FileField(upload_to='Sallaryslip')),
                ('selectbank', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 28, 2, 4, 33, 531773)),
        ),
    ]