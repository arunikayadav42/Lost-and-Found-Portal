# Generated by Django 2.1 on 2018-12-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('found', '0002_auto_20181202_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='found',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='found',
            name='brand',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='found',
            name='color',
            field=models.TextField(blank=True, null=True),
        ),
    ]
