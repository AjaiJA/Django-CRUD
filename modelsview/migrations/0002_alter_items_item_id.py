# Generated by Django 3.2 on 2021-06-29 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_id',
            field=models.IntegerField(),
        ),
    ]
