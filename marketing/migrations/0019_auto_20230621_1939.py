# Generated by Django 3.0.5 on 2023-06-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0018_auto_20230621_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale_order',
            name='sale_order_date',
            field=models.CharField(default='21-06-2023', max_length=10),
        ),
        migrations.AlterField(
            model_name='yard_despatchs',
            name='despatch_date',
            field=models.CharField(default='21-06-2023', max_length=10),
        ),
        migrations.AlterField(
            model_name='yardreceipts',
            name='received_date',
            field=models.CharField(default='21-06-2023', max_length=10),
        ),
    ]
