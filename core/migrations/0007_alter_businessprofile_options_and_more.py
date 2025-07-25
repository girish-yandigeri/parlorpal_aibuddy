# Generated by Django 5.2.3 on 2025-07-20 01:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_festival_customuser_email_verified_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="businessprofile",
            options={
                "verbose_name": "Business Profile",
                "verbose_name_plural": "Business Profiles",
            },
        ),
        migrations.AddField(
            model_name="festival",
            name="send_on_festival_day",
            field=models.BooleanField(
                default=True, help_text="Send notification on the festival day itself"
            ),
        ),
        migrations.AlterField(
            model_name="businessprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="businessprofile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
