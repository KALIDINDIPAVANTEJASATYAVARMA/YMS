# Generated by Django 3.0.5 on 2023-05-20 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_auto_20230520_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mktg_master',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='mktg_master',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='mktg_master',
            name='last_login',
        ),
    ]