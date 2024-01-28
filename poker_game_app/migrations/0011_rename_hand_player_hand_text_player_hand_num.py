# Generated by Django 5.0 on 2024-01-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker_game_app', '0010_alter_player_hand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='hand',
            new_name='hand_text',
        ),
        migrations.AddField(
            model_name='player',
            name='hand_num',
            field=models.IntegerField(null=True),
        ),
    ]