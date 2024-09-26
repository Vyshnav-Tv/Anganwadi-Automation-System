# Generated by Django 4.0.4 on 2023-01-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_id_gen_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_table',
            fields=[
                ('stud_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('anganw_id', models.CharField(max_length=30)),
                ('stud_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'student_table',
            },
        ),
    ]
