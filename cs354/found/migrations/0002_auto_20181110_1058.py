# Generated by Django 2.1 on 2018-11-10 10:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('found', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='found',
            old_name='date',
            new_name='date_item_registered',
        ),
        migrations.AddField(
            model_name='found',
            name='claimed',
            field=models.CharField(default='NC', max_length=2),
        ),
        migrations.AddField(
            model_name='found',
            name='date_item_found',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]