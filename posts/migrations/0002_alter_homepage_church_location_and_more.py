# Generated by Django 4.2.2 on 2023-06-17 14:03

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='church_location',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='mission',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='vision',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='ministers',
            name='word_of_encouragement',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='sermon_notes',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='upcomingevents',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 18, 14, 3, 6, 468032, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='upcomingevents',
            name='event_info',
            field=tinymce.models.HTMLField(),
        ),
    ]
