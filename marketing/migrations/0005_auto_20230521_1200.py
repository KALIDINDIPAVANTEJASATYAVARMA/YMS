# Generated by Django 3.0.5 on 2023-05-21 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_auto_20230520_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mktg_master',
            old_name='user_id',
            new_name='username',
        ),
    ]