# Generated by Django 4.2.2 on 2023-06-15 23:16

import cloudinary.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ministers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "minister_authority",
                    models.CharField(
                        choices=[
                            ("Apostle", "Apostle"),
                            ("Rev", "Rev"),
                            ("PST", "Pst"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("minister_name", models.CharField(max_length=100)),
                (
                    "minister_photo",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="image"
                    ),
                ),
                ("word_of_encouragement", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="PhotoGallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo_info", models.CharField(max_length=100)),
                ("date_taken", models.DateField(default=django.utils.timezone.now)),
                (
                    "photo",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="image"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UpcomingEvents",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("event_name", models.CharField(max_length=80)),
                (
                    "event_banner",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="image"
                    ),
                ),
                (
                    "event_date",
                    models.DateField(
                        default=datetime.datetime(
                            2023, 6, 16, 23, 16, 2, 481318, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                ("event_info", models.TextField()),
                ("pub_date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sermon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sermon_title", models.CharField(max_length=100)),
                ("sermon_date", models.DateField()),
                (
                    "sermon_time",
                    models.CharField(
                        choices=[
                            ("Morning", "Morning"),
                            ("Noon", "Noon"),
                            ("Evening", "Evening"),
                        ],
                        max_length=15,
                        null=True,
                    ),
                ),
                (
                    "sermon_youtube_link",
                    models.URLField(help_text='paste a youtube link "https://"'),
                ),
                ("sermon_notes", models.TextField(blank=True, null=True)),
                (
                    "preached_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="posts.ministers",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Homepage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "slide_photo_1",
                    cloudinary.models.CloudinaryField(
                        help_text="Enter upcoming event photo here",
                        max_length=255,
                        verbose_name="image",
                    ),
                ),
                (
                    "slide_photo_2",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="image"
                    ),
                ),
                (
                    "slide_photo_3",
                    cloudinary.models.CloudinaryField(
                        max_length=255, verbose_name="image"
                    ),
                ),
                ("service_1_name", models.CharField(max_length=100)),
                (
                    "service_1_day",
                    models.CharField(
                        help_text="enter the days of the week", max_length=30
                    ),
                ),
                ("service_1_start_time", models.TimeField()),
                ("service_2_name", models.CharField(max_length=100)),
                (
                    "service_2_day",
                    models.CharField(
                        help_text="enter the days of the week", max_length=30
                    ),
                ),
                ("service_2_start_time", models.TimeField()),
                ("service_3_name", models.CharField(max_length=100)),
                (
                    "service_3_day",
                    models.CharField(
                        help_text="enter the days of the week", max_length=30
                    ),
                ),
                ("service_3_start_time", models.TimeField()),
                ("service_4_name", models.CharField(max_length=100)),
                (
                    "service_4_day",
                    models.CharField(
                        help_text="enter the days of the week", max_length=30
                    ),
                ),
                ("service_4_start_time", models.TimeField()),
                ("church_location", models.TextField()),
                ("youtube_link_with_directions", models.URLField(null=True)),
                ("latest_sermon_youtube_link", models.URLField(null=True)),
                ("sermon_title", models.CharField(max_length=300, null=True)),
                ("latest_sermon_date", models.DateField(null=True)),
                ("event_1_name", models.CharField(max_length=100)),
                ("event_1_date", models.DateField()),
                ("event_1_start_time", models.TimeField()),
                ("event_1_location", models.CharField(max_length=200)),
                ("event_2_name", models.CharField(max_length=100)),
                ("event_2_date", models.DateField()),
                ("event_2_start_time", models.TimeField()),
                ("event_2_location", models.CharField(max_length=200)),
                ("event_3_name", models.CharField(max_length=100)),
                ("event_3_date", models.DateField()),
                ("event_3_start_time", models.TimeField()),
                ("event_3_location", models.CharField(max_length=200)),
                ("event_4_name", models.CharField(max_length=100)),
                ("event_4_date", models.DateField()),
                ("event_4_start_time", models.TimeField()),
                ("event_4_location", models.CharField(max_length=200)),
                ("vision", models.CharField(max_length=500)),
                ("mission", models.TextField()),
                ("latest_sermons", models.ManyToManyField(to="posts.sermon")),
                (
                    "preacher",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="posts.ministers",
                    ),
                ),
            ],
        ),
    ]
