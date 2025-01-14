# Generated by Django 4.0.4 on 2023-01-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_women_table_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='infant_table',
            fields=[
                ('inf_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('F_name', models.CharField(max_length=30)),
                ('M_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'infant_table',
            },
        ),
        migrations.CreateModel(
            name='vaccine_table',
            fields=[
                ('vac_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('discription', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'vaccine_table',
            },
        ),
        migrations.AddField(
            model_name='id_gen',
            name='infant_id',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='id_gen',
            name='vaccine_id',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]
