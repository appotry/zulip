# Generated by Django 3.2.4 on 2021-06-09 13:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0356_migrate_to_delete_own_message_policy"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="realm",
            name="allow_message_deleting",
        ),
    ]
