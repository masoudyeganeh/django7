# Generated by Django 4.2 on 2024-06-09 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalouge', '0004_alter_productattribute_attribute_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='attribute_type',
            field=models.PositiveSmallIntegerField(choices=[(2, 'STRING'), (3, 'FLOAT'), (1, 'INTEGER')], default=1),
        ),
    ]