# Generated by Django 4.0.4 on 2023-01-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_staf_table_angan_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staf_table',
            name='id_angan',
            field=models.CharField(default='0', max_length=30),
            preserve_default=False,
        ),
    ]
