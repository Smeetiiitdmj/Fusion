# Generated by Django 3.1.5 on 2023-04-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_mess', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthly_bill',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
