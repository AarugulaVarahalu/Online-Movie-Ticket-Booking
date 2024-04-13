# Generated by Django 4.2.11 on 2024-04-13 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve', models.PositiveIntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.movie')),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_at_showtime', to='content.showtime')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_at_theater', to='content.theater')),
            ],
        ),
    ]
