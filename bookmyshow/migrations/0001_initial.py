# Generated by Django 5.1 on 2024-09-10 18:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('director', models.CharField(max_length=50)),
                ('actors', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('row_number', models.IntegerField()),
                ('col_number', models.IntegerField()),
                ('number', models.IntegerField()),
                ('seat_type', models.CharField(choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('PLATINUM', 'Platinum')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.feature')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.movie')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.screen')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShowSeat',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('show_seat_status', models.CharField(choices=[('AVAILABLE', 'Available'), ('MAINTENANCE', 'Maintenance'), ('RESERVED', 'Reserved'), ('LOCKED', 'Locked'), ('FEMALEONLY', 'FemaleOnly')], max_length=50)),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.seat')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.show')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShowSeatType',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('seat_type', models.CharField(choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('PLATINUM', 'Platinum')], max_length=50)),
                ('price', models.IntegerField()),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.show')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='screen',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.theatre'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ticket_number', models.CharField(blank=True, max_length=12, unique=True)),
                ('amount', models.IntegerField()),
                ('booking_status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('WAITING', 'Waiting'), ('CANCELLED', 'Cancelled')], max_length=50)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.show')),
                ('show_seats', models.ManyToManyField(to='bookmyshow.showseat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ref_number', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('mode', models.CharField(choices=[('UPI', 'UPI'), ('CREDIT_CARD', 'Credit Card'), ('DEBIT_CARD', 'Debit Card'), ('NET_BANKING', 'Net Banking'), ('CASH', 'Cash')], max_length=50)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('WAITING', 'Waiting'), ('CANCELLED', 'Cancelled'), ('REFUNDED', 'Refunded')], max_length=50)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.ticket')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScreenFeature',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.feature')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyshow.screen')),
            ],
            options={
                'unique_together': {('screen', 'feature')},
            },
        ),
    ]
