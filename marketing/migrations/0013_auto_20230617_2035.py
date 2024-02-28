# Generated by Django 3.0.5 on 2023-06-17 15:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_product_master'),
        ('marketing', '0012_yard_receipts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yard_receipts',
            name='id',
        ),
        migrations.AddField(
            model_name='yard_receipts',
            name='product_id',
            field=models.ForeignKey(default='000000', on_delete=django.db.models.deletion.CASCADE, to='administrator.product_master', unique=True),
        ),
        migrations.AddField(
            model_name='yard_receipts',
            name='receipt_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='yard_receipts',
            name='received_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yard_receipts',
            name='received_qty',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='yard_receipts',
            name='remarks',
            field=models.CharField(default='good', max_length=60),
        ),
        migrations.AddField(
            model_name='yard_receipts',
            name='transport_type',
            field=models.CharField(default='truck', max_length=10),
        ),
    ]
