# Generated by Django 2.2 on 2020-09-10 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitizenshipDetails',
            fields=[
                ('citizenship_id', models.AutoField(primary_key=True, serialize=False)),
                ('citizenship_name', models.CharField(blank=True, max_length=100, null=True)),
                ('citizen_code', models.CharField(blank=True, max_length=3, null=True, unique=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('currency_code', models.CharField(max_length=5)),
                ('phone_code', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'citizenship_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CityMaster',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=40)),
                ('pos_code', models.CharField(blank=True, max_length=8, null=True)),
                ('country_code', models.CharField(blank=True, max_length=40, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'city_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorporateClosingBalance',
            fields=[
                ('closing_balance_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_corporate_id', models.IntegerField()),
                ('closed_date', models.DateTimeField()),
                ('r_currency_id', models.IntegerField()),
                ('closed_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('closed_by', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=1)),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'corporate_closing_balance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorporateDetails',
            fields=[
                ('corporate_id', models.AutoField(primary_key=True, serialize=False)),
                ('corporate_name', models.CharField(blank=True, max_length=99, null=True)),
                ('agent_name', models.CharField(blank=True, max_length=99, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=99, null=True)),
                ('branch_location', models.CharField(blank=True, max_length=99, null=True)),
                ('branch_pincode', models.CharField(blank=True, max_length=99, null=True)),
                ('parent_corporate_id', models.CharField(blank=True, max_length=20, null=True)),
                ('iata_code', models.CharField(blank=True, max_length=20, null=True)),
                ('pcc_code', models.CharField(blank=True, max_length=20, null=True)),
                ('airlines_code', models.CharField(blank=True, max_length=20, null=True)),
                ('r_currency_id', models.IntegerField(blank=True, null=True)),
                ('corporate_address', models.CharField(blank=True, max_length=99, null=True)),
                ('email_id', models.CharField(blank=True, max_length=99, null=True)),
                ('r_citizenship_id', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('r_city_id', models.IntegerField(blank=True, null=True)),
                ('corporate_status', models.CharField(blank=True, max_length=4, null=True)),
                ('office_number', models.BigIntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('time_zone_interval', models.IntegerField(blank=True, null=True)),
                ('time_zone_key', models.IntegerField(blank=True, null=True)),
                ('pos_code', models.CharField(blank=True, max_length=4, null=True)),
                ('fax', models.CharField(blank=True, max_length=10, null=True)),
                ('restrict_booking_status', models.CharField(blank=True, max_length=1, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('corporate_additional_info', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'corporate_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorporateGstDetails',
            fields=[
                ('corporate_gst_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_corporate_id', models.IntegerField(blank=True, null=True)),
                ('gst_email_id', models.CharField(blank=True, max_length=50, null=True)),
                ('gst_number', models.CharField(blank=True, max_length=50, null=True)),
                ('gst_address', models.CharField(blank=True, max_length=120, null=True)),
                ('mobile_no', models.BigIntegerField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=120, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'corporate_gst_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorporateGstLoginDetails',
            fields=[
                ('corporate_gst_login_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_corporate_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'corporate_gst_login_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CurrencyDetails',
            fields=[
                ('currency_id', models.AutoField(primary_key=True, serialize=False)),
                ('currency_code', models.CharField(blank=True, max_length=5, null=True)),
                ('currency_symbol', models.CharField(blank=True, max_length=5, null=True)),
                ('currency_display_name', models.CharField(blank=True, max_length=20, null=True)),
                ('exchange_rate', models.IntegerField(blank=True, null=True)),
                ('decimal_precision', models.IntegerField(blank=True, null=True)),
                ('display_order', models.IntegerField(blank=True, null=True)),
                ('currency_status', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'currency_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_group_id', models.PositiveIntegerField()),
                ('r_corporate_id', models.PositiveIntegerField()),
                ('r_status_id', models.PositiveIntegerField(blank=True, null=True)),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('time_zone', models.CharField(blank=True, max_length=30, null=True)),
                ('created_by', models.CharField(blank=True, max_length=12, null=True)),
                ('created_date', models.DateTimeField()),
                ('updated_by', models.CharField(blank=True, max_length=12, null=True)),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'user_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfileDetails',
            fields=[
                ('profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_user_id', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=5, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('email_id', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_profile_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserTypeMaster',
            fields=[
                ('user_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_type_name', models.CharField(max_length=30)),
                ('user_type_status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'user_type_master',
                'managed': False,
            },
        ),
    ]