# Generated by Django 5.0.6 on 2024-06-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_socialmedia_alter_service_whatsapp_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleMapsURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(blank=True, max_length=233)),
                ('url', models.URLField()),
            ],
        ),
    ]
