# Generated by Django 4.2 on 2024-11-19 12:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0002_category_transaction"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transaction",
            options={"ordering": ["-date"]},
        ),
    ]
