# Generated by Django 4.2.11 on 2024-04-13 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_reserve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('purchase', models.DecimalField(decimal_places=2, max_digits=5)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.movie')),
                ('reserve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_at_showtime', to='content.reserve')),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_at_showtime', to='content.showtime')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_at_theater', to='content.theater')),
            ],
        ),
    ]
