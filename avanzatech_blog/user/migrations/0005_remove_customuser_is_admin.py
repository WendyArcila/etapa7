# Generated by Django 5.0.4 on 2024-04-04 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customuser_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
    ]