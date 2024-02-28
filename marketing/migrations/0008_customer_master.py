# Generated by Django 3.0.5 on 2023-06-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0007_auto_20230521_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_master',
            fields=[
                ('customer_no', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(default='pavan', max_length=40)),
                ('customer_address', models.CharField(default='ukkunagaram', max_length=40)),
                ('city', models.CharField(default='vizag', max_length=40)),
                ('pin', models.IntegerField(default=530032, max_length=6)),
                ('phone_no', models.IntegerField(default=0, max_length=10)),
                ('email_id', models.CharField(default='abc@gmail.com', max_length=40)),
            ],
        ),
    ]
