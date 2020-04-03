# Generated by Django 3.0.3 on 2020-04-02 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mountainmapapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedMarker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('marker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mountainmapapi.Marker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ('saved_marker',),
                'verbose_name_plural': ('saved_markers',),
                'ordering': ('created_at',),
            },
        ),
    ]
