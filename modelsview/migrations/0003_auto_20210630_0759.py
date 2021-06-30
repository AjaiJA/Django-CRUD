# Generated by Django 3.2 on 2021-06-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsview', '0002_alter_items_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='items',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
