# Generated by Django 5.0 on 2023-12-24 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker_game_app', '0003_game_deck_game_num_players_game_river_cards_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='card1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='card2',
            field=models.CharField(max_length=10, null=True),
        ),
    ]