# Generated by Django 4.0.3 on 2022-10-12 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0003_alter_user_data_last_menstural_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_data',
            old_name='last_menstural_data',
            new_name='last_menstural_date',
        ),
    ]
