# Generated by Django 4.2.11 on 2024-04-26 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postgresdb', '0006_remove_item_tags_item_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='available_stock',
            new_name='availableStock',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='stock_status',
            new_name='inStock',
        ),
    ]