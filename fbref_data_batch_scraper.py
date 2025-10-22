import pandas as pd

# EPL for league teams data
def epl_for_league_data(szn_yrs):
    # EPL league table
    try:
        epl_overall = pd.read_html("https://fbref.com/en/comps/9/"+szn_yrs[0]+"-"+szn_yrs[1]+"/"+szn_yrs[0]+"-"+szn_yrs[1]+"-Premier-League-Stats",
                                   attrs={"id": "results"+szn_yrs[0]+"-"+szn_yrs[1]+"91_overall"})[0] \
                                    .drop(columns=["Notes", "Unnamed: 0"]).set_index("Rk", inplace=True)
        print("FBref EPL overall data downloaded and uploaded to excel file")
    except:
        epl_overall = pd.DataFrame()
        print("No new Fbref overall data acquired")
    # EPL standard stats
    try: 
        epl_squad_stats_for = pd.read_html("https://fbref.com/en/comps/9/"+szn_yrs[0]+"-"+szn_yrs[1]+"/"+szn_yrs[0]+"-"+szn_yrs[1]+"-Premier-League-Stats",
                                           attrs={"id": "stats_squads_standard_for"})[0]
        print("FBref EPL squad data downloaded and uploaded to excel file")
    except:
        epl_squad_stats_for = pd.DataFrame()
        print("No new Fbref squad data acquired")
    # EPL team possesion stats
    try: 
        epl_squad_poss_for = pd.read_html("https://fbref.com/en/comps/9/"+szn_yrs[0]+"-"+szn_yrs[1]+"/"+szn_yrs[0]+"-"+szn_yrs[1]+"-Premier-League-Stats",
                                          attrs={"id": "stats_squads_possession_for"})[0]
        print("FBref EPL team possession data downloaded and uploaded to excel file")
    except:
        epl_squad_poss_for = pd.DataFrame()
        print("No new Fbref overall data acquired")
    # EPL shooting stats
    try:
        epl_squad_shooting_for = pd.read_html("https://fbref.com/en/comps/9/"+szn_yrs[0]+"-"+szn_yrs[1]+"/"+szn_yrs[0]+"-"+szn_yrs[1]+"-Premier-League-Stats",
                                              attrs={"id": "stats_squads_shooting_for"})[0]
        print("FBref EPL squad shooting data downloaded")
    except:
        epl_squad_shooting_for = pd.DataFrame()
        print("No new Fbref squad shooting data acquired")
    # EPL goal and shot creation stats
    try:
        epl_squad_goal_shot_crt_for = pd.read_html("https://fbref.com/en/comps/9/"+szn_yrs[0]+"-"+szn_yrs[1]+"/"+szn_yrs[0]+"-"+szn_yrs[1]+"-Premier-League-Stats",
                                                   attrs={"id": "stats_squads_shooting_creation_for"})[0]
        print("FBref EPL squad goal/shot creation data downloaded")
    except:
        epl_squad_goal_shot_crt_for = pd.DataFrame()
        print("No new Fbref squad goal/shot creation data acquired")
    # EPL defensive actions stats
    try:
        epl_def_actns_for = pd.read_html("https://fbref.com/en/comps/9/"+szn_yrs[0]+"-"+szn_yrs[1]+"/"+szn_yrs[0]+"-"+szn_yrs[1]+"-Premier-League-Stats",
                                         attrs={"id": "stats_squads_defense_for"})[0]
        print("FBref EPL squad defensive actions data downloaded")
    except:
        epl_def_actns_for = pd.DataFrame()
        print("No new Fbref squad defensive actions data acquired")
    # all tables placed within an array (python list)
    epl_gen_teams_data = [
        epl_overall,
        epl_squad_stats_for,
        epl_squad_poss_for,
        epl_squad_shooting_for,
        epl_squad_goal_shot_crt_for,
        epl_def_actns_for,
    ]
    return epl_gen_teams_data

