# Generated by Django 4.2.7 on 2023-11-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nuarte", "0005_remove_instrumento_historico_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="instrumento",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="instrumentos/"),
        ),
    ]
