# Generated by Django 3.2.5 on 2021-08-01 08:08

from django.conf import settings
import django.contrib.postgres.fields.citext
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django.contrib.postgres.fields.citext.CICharField(max_length=64, verbose_name='name')),
                ('description', models.TextField(max_length=1024, verbose_name='description')),
                ('currency', models.PositiveSmallIntegerField(choices=[(1, 'USD, $'), (2, 'EUR, €'), (3, 'RUB, ₽'), (4, 'UAH, ₴'), (5, 'BYN, Br')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='currency')),
                ('require_phone_num', models.PositiveSmallIntegerField(choices=[(1, 'Always'), (2, 'Never'), (3, 'If delivery is selected')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='require phone number')),
                ('delivery', models.BooleanField(default=False, verbose_name='is delivery available')),
                ('min_delivery_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='minimum price for delivery')),
                ('image', models.ImageField(blank=True, null=True, upload_to='shops/', verbose_name='image')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'shop',
                'verbose_name_plural': 'shops',
            },
        ),
    ]
