# Generated by Django 2.2 on 2022-07-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestResponseRestapi',
            fields=[
                ('request_response_id', models.AutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=10)),
                ('request_data', models.TextField()),
                ('response_data', models.TextField(blank=True, null=True)),
                ('request_time', models.DateTimeField()),
                ('response_time', models.DateTimeField(blank=True, null=True)),
                ('time_different', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'request_response_restapi',
                'managed': False,
            },
        ),
    ]