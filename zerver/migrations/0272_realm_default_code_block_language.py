# Generated by Django 2.2.10 on 2020-03-31 00:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0271_huddle_set_recipient_column_values"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="default_code_block_language",
            field=models.TextField(default=None, null=True),
        ),
    ]
