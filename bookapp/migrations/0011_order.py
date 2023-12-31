# Generated by Django 4.2 on 2023-09-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0010_users_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('user_firstname', models.CharField(max_length=50)),
                ('user_lastname', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('user_company', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=50)),
                ('user_city', models.CharField(max_length=50)),
                ('user_zipcode', models.IntegerField()),
                ('order_cost', models.IntegerField()),
                ('order_cart', models.JSONField(default={})),
                ('timestamp', models.PositiveBigIntegerField()),
            ],
        ),
    ]
