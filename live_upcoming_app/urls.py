from django.urls import path
from .views  import *
from live_upcoming_app import views

urlpatterns=[
# Events&LiveMatch
    path('InternetionalEvent/', views.InternationalEvent, name='InternetionalEvent'),
    path('Live_Interntonal/', views.live_international, name='Live_Interntonal'),

# MensRanking
    path('BatMenTestRanking/', views.NewsView6, name='BatMenTestRanking'),
    path('BatMenODIRanking/', views.NewsView7, name='BatMenODIRanking'),
    path('BatMenT20Ranking/', views.NewsView8, name='BatMenT20Ranking'),
    path('bowlerMenTestRanking/', views.NewsView9, name='bowlerMenTestRanking'),
    path('bowlerMenODIRanking/', views.NewsView10, name='bowlerMenODIRanking'),
    path('bowlerMenT20Ranking/', views.NewsView11, name='bowlerMenT20Ranking'),
    path('AllrounderMenTestRanking/', views.NewsView12, name='AllrounderMenTestRanking'),
    path('AllrounderMenODIRanking/', views.NewsView13, name='AllrounderMenODIRanking'),
    path('AllrounderMenT20Ranking/', views.NewsView14, name='AllrounderMenT20Ranking'),

#WomensRanking
    path('BatWoMenODIRanking/', views.WomenODIbat, name='BatWoMenODIRanking'),
    path('BowlerWoMenODIRanking/', views.WomenODIbowler, name='BowlerWoMenODIRanking'),
    path('AllrounderWoMenODIRanking/', views.WomenODIAllrounder, name='AllrounderWoMenODIRanking'),
    path('WomenT20Bowler/', views.WomenT20Bowler, name='WomenT20Bowler'),
    path('WomenT20Bat/', views.WomenT20Bat, name='WomenT20Bat'),
    path('WomenT20Allrounder/', views.WomenT20Allrounder, name='WomenT20Allrounder'),
    path('WomenT20Teams/', views.WomenT20Teams, name='WomenT20Teams'),
    path('WomenODITeams/', views.WomenODITeams, name='WomenODITeams'),

#menTeamsRankings
    path('MenTeamsTestRanking/', views.MenTestTeams, name='MenTeamsTestRanking'),
    path('MenODITeamsRanking/', views.MenODITeams, name='MenODITeamsRanking'),
    path('MenT20TeamsRanking/', views.MenT20Teams, name='MenT20TeamsRanking'),

#commentry,overs,scoreboard
    # path('commentry/', views.commentry, name='commentry'),
    # path('overs/', views.overs, name='overs'),
    path('scorecard/', views.scorecard, name='scorecard'),

]