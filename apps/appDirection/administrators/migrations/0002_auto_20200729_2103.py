# Generated by Django 3.0.6 on 2020-07-30 02:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrators', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Teacher',
            new_name='Administrator',
        ),
    ]