# Generated by Django 4.2 on 2024-05-02 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0016_message_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mailings.client', verbose_name='Клиент'),
            preserve_default=False,
        ),
    ]
