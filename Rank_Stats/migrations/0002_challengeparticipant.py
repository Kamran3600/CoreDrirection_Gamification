# Generated by Django 4.1.13 on 2024-01-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_direction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeParticipant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('profile_picture', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=1)),
                ('privacy', models.CharField(max_length=20)),
                ('totalCorePoints', models.IntegerField()),
                ('stepCounts', models.IntegerField()),
                ('totalWatchedVideoToday', models.IntegerField()),
                ('checkins', models.IntegerField()),
                ('heartRate', models.IntegerField()),
                ('totalActivityLogToday', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('numberOfParticipent', models.IntegerField()),
                ('challengeId', models.IntegerField()),
                ('challengeSlug', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'challengeparticipantschemas',
            },
        ),
    ]
