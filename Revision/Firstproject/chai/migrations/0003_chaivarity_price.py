# Generated by Django 5.1.6 on 2025-03-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_chaivarity_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='price',
            field=models.DecimalField(decimal_places=2, default=50.0, max_digits=5),
        ),
    ]
