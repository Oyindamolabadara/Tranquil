# Generated by Django 3.2.13 on 2022-08-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]