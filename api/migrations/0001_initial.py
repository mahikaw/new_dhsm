# Generated by Django 2.1.2 on 2018-10-08 09:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asha_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='family_profile',
            fields=[
                ('anm', models.CharField(max_length=50)),
                ('health_facility', models.CharField(max_length=100)),
                ('area_code', models.IntegerField()),
                ('area_description', models.TextField()),
                ('date_of_survey', models.DateField(default=django.utils.timezone.now)),
                ('name_head_of_family', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=6)),
                ('mobile_no', models.CharField(max_length=10)),
                ('landline', models.CharField(max_length=8)),
                ('category', models.CharField(choices=[('1', 'General'), ('2', 'SC'), ('3', 'ST'), ('4', 'Other')], max_length=1)),
                ('religion', models.CharField(choices=[('1', 'Hindu'), ('2', 'Muslim'), ('3', 'Sikh'), ('4', 'Isai'), ('5', 'Other')], max_length=1)),
                ('family_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('asha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.asha')),
            ],
        ),
    ]
