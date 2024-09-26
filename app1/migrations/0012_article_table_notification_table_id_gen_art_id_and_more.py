# Generated by Django 4.0.4 on 2023-02-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_infant_table_vaccine_table_id_gen_infant_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='article_table',
            fields=[
                ('arti_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('id_ang', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('photo', models.CharField(max_length=30)),
                ('num_of_items', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'article_table',
            },
        ),
        migrations.CreateModel(
            name='notification_table',
            fields=[
                ('notifi_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('notification', models.CharField(max_length=90)),
                ('not_dt', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'notification_table',
            },
        ),
        migrations.AddField(
            model_name='id_gen',
            name='art_id',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='id_gen',
            name='noti_id',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]