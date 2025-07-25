# Generated by Django 5.2.3 on 2025-07-19 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_businessprofile_location_businessprofile_phone_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Festival",
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
                    "name",
                    models.CharField(help_text="Name of the festival", max_length=100),
                ),
                ("date", models.DateField(help_text="Date of the festival")),
                (
                    "notification_days",
                    models.IntegerField(
                        default=3, help_text="Days before festival to send notification"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Whether this festival is active for notifications",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["date"],
            },
        ),
        migrations.AddField(
            model_name="customuser",
            name="email_verified",
            field=models.BooleanField(
                default=False, help_text="Whether the user's email has been verified"
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="notifications_enabled",
            field=models.BooleanField(
                default=False, help_text="Whether user wants festival notifications"
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="token_created_at",
            field=models.DateTimeField(
                blank=True,
                help_text="When the verification token was created",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="verification_token",
            field=models.CharField(
                blank=True, help_text="Token for email verification", max_length=100
            ),
        ),
    ]
