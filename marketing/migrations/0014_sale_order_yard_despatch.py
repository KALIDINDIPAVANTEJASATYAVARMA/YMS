# Generated by Django 3.0.5 on 2023-06-17 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_product_master'),
        ('marketing', '0013_auto_20230617_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='sale_order',
            fields=[
                ('sale_order_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('sale_order_date', models.DateField(default='timezone.now')),
                ('sale_order_qty', models.IntegerField(default=1000)),
                ('remarks', models.CharField(default='good', max_length=60)),
                ('customer_id', models.ForeignKey(default='000000', on_delete=django.db.models.deletion.CASCADE, to='marketing.customer_master', unique=True)),
                ('product_id', models.ForeignKey(default='000000', on_delete=django.db.models.deletion.CASCADE, to='administrator.product_master', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='yard_despatch',
            fields=[
                ('despatch_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('transport_type', models.CharField(default='truck', max_length=10)),
                ('despatch_date', models.DateField(default='timezone.now')),
                ('despatched_qty', models.IntegerField(default=1000)),
                ('remarks', models.CharField(default='good', max_length=60)),
                ('sale_order_id', models.ForeignKey(default='000000', on_delete=django.db.models.deletion.CASCADE, to='marketing.sale_order', unique=True)),
                ('yard_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.customer_master')),
            ],
        ),
    ]
