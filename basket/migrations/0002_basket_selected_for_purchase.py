# Generated by Django 5.0.1 on 2024-03-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='selected_for_purchase',
            field=models.BooleanField(default=True),
        ),
    ]
