# Generated by Django 4.0.4 on 2023-02-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_message_table_id_gen_mess_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification_table',
            name='an_id',
            field=models.CharField(default='0', max_length=90),
            preserve_default=False,
        ),
    ]
