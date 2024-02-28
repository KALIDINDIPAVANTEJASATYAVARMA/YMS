# Generated by Django 3.0.5 on 2023-06-23 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_product_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='transport_master',
            fields=[
                ('driver_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('vehicle_type', models.CharField(default='truck', max_length=5)),
                ('driver_name', models.CharField(default='xyz', max_length=40)),
                ('email_id', models.CharField(default=0, max_length=20)),
                ('phone_no', models.CharField(default=0, max_length=10)),
            ],
        ),
    ]
