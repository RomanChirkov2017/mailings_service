# Generated by Django 4.2 on 2024-05-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0013_alter_mailingsettings_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='last_send',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последней отправки'),
        ),
    ]
