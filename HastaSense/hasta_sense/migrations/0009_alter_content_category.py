# Generated by Django 5.0.3 on 2024-04-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hasta_sense", "0008_alter_content_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="category",
            field=models.IntegerField(),
        ),
    ]
