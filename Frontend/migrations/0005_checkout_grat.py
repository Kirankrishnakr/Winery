# Generated by Django 4.1.7 on 2023-07-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='Grat',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
