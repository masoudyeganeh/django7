# Generated by Django 4.2 on 2024-06-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalouge', '0002_producttype_created_time_producttype_updated_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='attribute_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'INTEGER'), (2, 'STRING'), (3, 'FLOAT')], default=1),
        ),
    ]