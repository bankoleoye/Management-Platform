# Generated by Django 4.0.4 on 2022-04-28 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_user_is_admin_alter_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(default=0, max_length=15, unique=True),
        ),
    ]
