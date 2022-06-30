# Generated by Django 4.0.5 on 2022-06-30 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news_blog', '0023_poststatusrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='postrecycle',
            name='recycle_created_on',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='poststatusrecord',
            name='changed_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='postview',
            name='viewed_on',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
