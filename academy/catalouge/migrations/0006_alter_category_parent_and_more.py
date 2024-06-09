# Generated by Django 4.2 on 2024-06-09 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalouge', '0005_alter_productattribute_attribute_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalouge.category'),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='attribute_type',
            field=models.PositiveSmallIntegerField(choices=[(3, 'FLOAT'), (1, 'INTEGER'), (2, 'STRING')], default=1),
        ),
    ]