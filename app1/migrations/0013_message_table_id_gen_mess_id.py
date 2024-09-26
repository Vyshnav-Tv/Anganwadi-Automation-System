# Generated by Django 4.0.4 on 2023-02-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_article_table_notification_table_id_gen_art_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='message_table',
            fields=[
                ('messg_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=90)),
                ('message', models.CharField(max_length=90)),
                ('messg_dt', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'message_table',
            },
        ),
        migrations.AddField(
            model_name='id_gen',
            name='mess_id',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]