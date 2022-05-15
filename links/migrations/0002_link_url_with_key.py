# Generated by Django 4.0.4 on 2022-05-15 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="link",
            index=models.Index(fields=["url_address", "key"], name="url_with_key"),
        ),
    ]
