# Generated by Django 4.0.3 on 2022-10-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0002_user_data_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='last_menstural_data',
            field=models.DateField(null=True),
        ),
    ]