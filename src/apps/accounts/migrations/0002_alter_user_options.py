# Generated by Django 4.2.7 on 2024-08-22 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ["-pk"], "verbose_name": "유저", "verbose_name_plural": "유저"},
        ),
    ]
