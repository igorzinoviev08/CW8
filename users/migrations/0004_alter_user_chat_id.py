# Generated by Django 4.2.5 on 2023-10-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chat_id',
            field=models.CharField(default=0, max_length=20, verbose_name='ID чат в tg'),
        ),
    ]
