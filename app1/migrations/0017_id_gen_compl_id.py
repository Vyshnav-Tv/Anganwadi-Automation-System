# Generated by Django 4.0.4 on 2023-02-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_foodallotment_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='id_gen',
            name='compl_id',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]