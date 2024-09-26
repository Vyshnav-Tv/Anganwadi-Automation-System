# Generated by Django 4.0.4 on 2023-01-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_student_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='women_table',
            fields=[
                ('women_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('agn_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('d_date', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'women_table',
            },
        ),
        migrations.AddField(
            model_name='id_gen',
            name='prg_women_id',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]
