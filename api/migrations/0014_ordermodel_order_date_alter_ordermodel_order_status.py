# Generated by Django 4.1.7 on 2023-03-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0013_alter_ordermodel_order_items_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordermodel",
            name="order_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="ordermodel",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("Wait", "Ожидает звонка"),
                    ("API", "Заказ передан клиенту"),
                    ("Cancel", "Заказ отменён клиентом"),
                ],
                default="Wait",
                max_length=50,
                null=True,
            ),
        ),
    ]
