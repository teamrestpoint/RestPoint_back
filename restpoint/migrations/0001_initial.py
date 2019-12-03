# Generated by Django 3.0 on 2019-12-02 22:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=250)),
                ('image_url', models.CharField(blank=True, max_length=250)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('address', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('directions', models.TextField(blank=True, null=True)),
                ('has_changing_table', models.BooleanField()),
                ('is_accessible', models.BooleanField()),
                ('is_gender_neutral', models.BooleanField()),
                ('is_family_bathroom', models.BooleanField()),
                ('number_of_stalls', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('review_text', models.TextField(blank=True, null=True)),
                ('is_accurate', models.BooleanField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='restpoint.Location')),
            ],
        ),
    ]