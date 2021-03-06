# Generated by Django 3.0.3 on 2020-04-02 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('lat', models.CharField(max_length=20, null=True)),
                ('long', models.CharField(max_length=20, null=True)),
                ('is_public', models.BooleanField()),
                ('description', models.CharField(max_length=100, null=True)),
                ('picture_url', models.CharField(max_length=25, null=True)),
            ],
            options={
                'verbose_name': ('order',),
                'verbose_name_plural': ('orders',),
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='MarkerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='TripPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': ('order',),
                'verbose_name_plural': ('orders',),
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='TripPlanMarker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mountainmapapi.Marker')),
                ('trip_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mountainmapapi.TripPlan')),
            ],
            options={
                'ordering': ('marker',),
            },
        ),
        migrations.AddField(
            model_name='tripplan',
            name='markers',
            field=models.ManyToManyField(through='mountainmapapi.TripPlanMarker', to='mountainmapapi.Marker'),
        ),
        migrations.AddField(
            model_name='tripplan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='marker',
            name='marker_type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mountainmapapi.MarkerType'),
        ),
        migrations.AddField(
            model_name='marker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
