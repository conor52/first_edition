# Generated by Django 3.1.3 on 2020-12-14 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='User_Profile',
            new_name='user_profile',
        ),
    ]