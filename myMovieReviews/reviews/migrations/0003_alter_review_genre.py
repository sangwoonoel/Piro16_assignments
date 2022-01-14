# Generated by Django 4.0.1 on 2022-01-14 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.CharField(choices=[('AC', 'Action'), ('SF', 'SF'), ('CO', 'Comedy'), ('RO', 'Romedy'), ('TH', 'Thriller'), ('HO', 'Horror'), ('WA', 'War'), ('SP', 'Sports'), ('MU', 'Musical'), ('ME', 'Melodrama'), ('AN', 'Animation'), (' CR', 'Crime')], max_length=50, verbose_name='장르'),
        ),
    ]
