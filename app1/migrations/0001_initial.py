# Generated by Django 4.0.4 on 2023-01-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anganwadi_table',
            fields=[
                ('angan_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('dist', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('build_num', models.CharField(max_length=30)),
                ('owner_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'anganwadi_table',
            },
        ),
        migrations.CreateModel(
            name='id_gen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anganwadi_id', models.IntegerField()),
            ],
            options={
                'db_table': 'id_gen',
            },
        ),
    ]
