# Generated by Django 4.2 on 2023-09-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0014_purchased_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchased_books',
            name='userid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
