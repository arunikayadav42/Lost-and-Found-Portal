# Generated by Django 2.1 on 2018-12-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0002_auto_20181202_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='lost',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lost',
            name='brand',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lost',
            name='color',
            field=models.TextField(blank=True, null=True),
        ),
    ]
