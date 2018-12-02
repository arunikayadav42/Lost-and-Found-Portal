# Generated by Django 2.1 on 2018-12-02 14:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Lost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('brand', models.TextField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_item_lost', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_item_registered', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')),
            ],
        ),
    ]
