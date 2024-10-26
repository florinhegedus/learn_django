# Generated by Django 5.0.9 on 2024-10-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('subscriptions', '0002_alter_subscriptions_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('groups', models.ManyToManyField(to='auth.group')),
            ],
            options={
                'permissions': [('advanced', 'Advanced Perm'), ('pro', 'Pro Perm'), ('basic', 'Basic Perm'), ('basic_ai', 'Basic AI Perm')],
            },
        ),
        migrations.DeleteModel(
            name='Subscriptions',
        ),
    ]