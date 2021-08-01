# Generated by Django 3.2.5 on 2021-08-01 08:08

import django.contrib.postgres.fields.citext
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeleUser',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('phone_num', models.CharField(blank=True, max_length=18, null=True, verbose_name='phone number')),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='user id in telegram')),
                ('username', django.contrib.postgres.fields.citext.CICharField(blank=True, max_length=36, null=True, verbose_name='username')),
            ],
            options={
                'verbose_name': 'telegram user',
                'verbose_name_plural': 'telegram users',
            },
        ),
        migrations.CreateModel(
            name='TeleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending'), (2, 'Shipped'), (3, 'Completed'), (4, 'Declined'), (5, 'Canceled'), (6, 'Refunded')], null=True, verbose_name='status')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.coupon', verbose_name='coupon')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product', verbose_name='product')),
                ('teleuser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='telegram.teleuser', verbose_name='telegram user')),
            ],
            options={
                'verbose_name': 'Telegram order',
                'verbose_name_plural': 'Telegram orders',
            },
        ),
        migrations.CreateModel(
            name='TeleBot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('username', django.contrib.postgres.fields.citext.CICharField(max_length=60, unique=True, verbose_name='bot name')),
                ('token', django.contrib.postgres.fields.citext.CICharField(max_length=36, unique=True, verbose_name='token')),
                ('shop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shops.shop', verbose_name='shop')),
            ],
            options={
                'verbose_name': 'telegram bot',
                'verbose_name_plural': 'telegram bots',
            },
        ),
    ]
