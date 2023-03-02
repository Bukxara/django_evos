# Generated by Django 4.1.7 on 2023-03-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0008_ordermodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordermodel",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("API", "Заказ передан клиенту"),
                    ("Cancel", "Заказ отменён клиентом"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="ordermodel",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("Наличные", "Наличные"),
                    ("Click", "Click"),
                    ("Payme", "Payme"),
                ],
                max_length=20,
            ),
        ),
    ]
