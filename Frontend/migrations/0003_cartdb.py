# Generated by Django 4.1.7 on 2023-06-24 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_signupdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(blank=True, max_length=60, null=True)),
                ('Product', models.CharField(blank=True, max_length=70, null=True)),
                ('Pprice', models.CharField(blank=True, max_length=50, null=True)),
                ('Quan', models.IntegerField(blank=True, null=True)),
                ('Tot', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]
