# Generated by Django 4.2.1 on 2023-05-07 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_author_blog_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="created_at",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
