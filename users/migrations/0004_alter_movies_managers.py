# Generated by Django 4.1.1 on 2022-09-23 12:59

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_rename_name_viewers_vname"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="movies",
            managers=[
                ("custome_obj", django.db.models.manager.Manager()),
            ],
        ),
    ]
