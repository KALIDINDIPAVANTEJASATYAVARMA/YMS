# Generated by Django 3.0.5 on 2023-06-18 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0015_auto_20230617_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yard_receipts',
            name='yard_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.yard_master'),
        ),
    ]
