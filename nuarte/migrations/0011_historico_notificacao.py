# Generated by Django 4.2.7 on 2023-12-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nuarte", "0010_remove_instrumento_usuario"),
    ]

    operations = [
        migrations.AddField(
            model_name="historico",
            name="notificacao",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
