# Generated by Django 4.2.5 on 2023-09-11 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'get_latest_by': 'title', 'ordering': ['title']},
        ),
    ]
