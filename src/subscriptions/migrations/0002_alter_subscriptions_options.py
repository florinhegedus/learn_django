# Generated by Django 5.0.9 on 2024-10-26 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriptions',
            options={'permissions': [('advanced', 'Advanced Perm'), ('pro', 'Pro Perm'), ('basic', 'Basic Perm'), ('basic_ai', 'Basic AI Perm')]},
        ),
    ]
