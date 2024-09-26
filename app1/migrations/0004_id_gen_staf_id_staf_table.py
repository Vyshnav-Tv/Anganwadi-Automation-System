# Generated by Django 4.0.4 on 2023-01-18 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_login_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='id_gen',
            name='staf_id',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='staf_table',
            fields=[
                ('stf_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('staf_name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('photo', models.CharField(max_length=30)),
                ('angan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.anganwadi_table')),
            ],
            options={
                'db_table': 'staf_table',
            },
        ),
    ]
