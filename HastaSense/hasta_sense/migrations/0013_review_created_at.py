# Generated by Django 5.0.3 on 2024-05-03 03:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hasta_sense", "0012_remove_review_created_at_alter_review_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]