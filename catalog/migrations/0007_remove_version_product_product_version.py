# Generated by Django 4.2.2 on 2023-07-18 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.version'),
        ),
    ]
