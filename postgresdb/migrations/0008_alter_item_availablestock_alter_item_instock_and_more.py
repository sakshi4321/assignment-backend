# Generated by Django 4.2.11 on 2024-04-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgresdb', '0007_rename_available_stock_item_availablestock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='availableStock',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='inStock',
            field=models.IntegerField(),
        ),
        migrations.RemoveField(
            model_name='item',
            name='tags',
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='postgresdb.tag'),
        ),
    ]
