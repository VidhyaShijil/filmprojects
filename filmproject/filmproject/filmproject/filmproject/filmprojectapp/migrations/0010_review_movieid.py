# Generated by Django 5.0.3 on 2024-04-01 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmprojectapp', '0009_review_delete_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movieid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
