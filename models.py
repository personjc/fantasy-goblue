from django.db import models

class Manager(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)

class Season(models.Model):
    season = models.IntegerField(primary_key=True)
    league_id = models.IntegerField()
    game_id = models.IntegerField()

class SeasonStandings(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT)
    team_name = models.CharField(max_length=30)
    season = models.ForeignKey(Season, models.PROTECT)
    league_wins = models.IntegerField()
    league_losses = models.IntegerField()
    points_for = models.DecimalField(max_digits=6, decimal_places=2)
    points_against = models.DecimalField(max_digits=6, decimal_places=2)

class TeamWeekInfo(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT)
    season = models.ForeignKey(Season, on_delete=models.PROTECT)
    week = models.IntegerField()
    etew_wins = models.IntegerField()
    etew_losses = models.IntegerField()
    week_score = models.DecimalField(max_digits=5, decimal_places=2)
    roster_json = models.JSONField()