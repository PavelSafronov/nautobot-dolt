# Generated by Django 3.2.17 on 2023-02-17 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_token_ordering_by_created"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ["username"]},
        ),
    ]
