# Generated by Django 4.1.7 on 2023-06-05 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("video", "0003_alter_video_avatarurl_alter_video_coverurl_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="video",
            old_name="userId",
            new_name="userID",
        ),
    ]