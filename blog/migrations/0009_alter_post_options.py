# Generated by Django 4.2.5 on 2023-09-11 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': '-created_at', 'ordering': ['-created_at']},
        ),
    ]
