# Generated by Django 5.0.3 on 2024-04-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hasta_sense", "0002_rename_alphabet_title_content_content_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="content_sign_video",
            field=models.FileField(
                default="default_video.mp4",
                upload_to="sign_images/content_sign_videos/",
            ),
        ),
    ]
