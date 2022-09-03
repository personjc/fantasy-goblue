from rest_framework import serializers
from .models import Manager, Season, SeasonStandings, TeamWeekInfo

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'name']

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['season', 'league_id', 'game_id']



class SeasonStandingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonStandings
        fields = ['manager', 'team_name', 'season', 'league_wins', 'league_losses', 'points_for', 'points_against']

class TeamWeekInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamWeekInfo
        fields = ['manager', 'season', 'week', 'etew_wins', 'etew_losses', 'week_score', 'roster_json']