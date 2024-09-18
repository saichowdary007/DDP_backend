# Generated by Django 4.2 on 2024-09-18 12:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("ddpui", "0100_llmsession_feedback"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConnectionJob",
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
                    "created_at",
                    models.DateTimeField(
                        auto_created=True, default=django.utils.timezone.now
                    ),
                ),
                ("connection_id", models.CharField(max_length=36)),
                ("job_type", models.CharField(max_length=36)),
                ("scheduled_at", models.DateTimeField()),
                ("flow_run_id", models.CharField(max_length=36)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ConnectionMeta",
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
                ("connection_id", models.CharField(max_length=36)),
                ("schedule_large_jobs", models.BooleanField(default=True)),
            ],
        ),
    ]
