# Generated by Django 3.1.1 on 2021-02-22 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igreja', '0004_auto_20210222_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='lideres',
            name='contato',
            field=models.CharField(default=2222, max_length=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lideres',
            name='descricao',
            field=models.TextField(default='deadaedaed'),
            preserve_default=False,
        ),
    ]
