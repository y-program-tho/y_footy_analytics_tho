import pandas as pd

# EPL for league teams data scraped from Fbref based on the szn_yrs input
def epl_for_league_data(szn_yrs):
    # 1 - EPL league table
    try:
        epl_overall_for = pd.read_html("https://fbref.com/en/comps/9/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"-Premier-League-Stats",
                                   attrs={"id": "results"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"91_overall"})[0].set_index("Rk")
        epl_overall_for = epl_overall_for[['Squad', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts', 'Pts/MP', 'xG','xGA', 'xGD']]
        print("FBref EPL overall data downloaded and uploaded to excel file")
    except:
        epl_overall_for = pd.DataFrame()
        print("No new Fbref overall data acquired")
    # 2 - EPL standard stats
    try: 
        epl_squad_stats_for = pd.read_html("https://fbref.com/en/comps/9/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"-Premier-League-Stats",
                                           attrs={"id": "stats_squads_standard_for"})[0]
        epl_squad_stats_for = epl_squad_stats_for[['Squad', '# Pl', 'Age', 'Poss', 'Playing Time MP', 'Playing Time Starts', 'Playing Time Min', 'Playing Time 90s', 'Performance Gls',
                                                   'Performance Ast', 'Performance G+A', 'Performance G-PK', 'Performance PK', 'Performance PKatt', 'Performance CrdY', 'Performance CrdR', 
                                                   'Expected xG', 'Expected npxG','Expected xAG', 'Expected npxG+xAG', 'Progression PrgC', 'Progression PrgP', 'Per 90 Minutes Gls', 'Per 90 Minutes Ast',
                                                   'Per 90 Minutes G+A', 'Per 90 Minutes G-PK', 'Per 90 Minutes G+A-PK','Per 90 Minutes xG', 'Per 90 Minutes xAG', 'Per 90 Minutes xG+xAG', 
                                                   'Per 90 Minutes npxG', 'Per 90 Minutes npxG+xAG']]
        print("FBref EPL squad data downloaded and uploaded to excel file")
    except:
        epl_squad_stats_for = pd.DataFrame()
        print("No new Fbref squad data acquired")
    # 3 - EPL squad shooting stats
    try:
        epl_squad_shooting_for = pd.read_html("https://fbref.com/en/comps/9/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"-Premier-League-Stats",
                                              attrs={"id": "stats_squads_shooting_for"})[0]
        epl_squad_shooting_for = epl_squad_shooting_for[['Squad', 'Poss', '90s', 'Touches Touches', 'Touches Def 3rd', 'Touches Mid 3rd', 'Touches Att 3rd',
                                                         'Touches Att Pen', 'Touches Live', 'Take-Ons Att', 'Take-Ons Succ','Take-Ons Succ%', 'Take-Ons Tkld', 
                                                         'Take-Ons Tkld%', 'Carries Carries', 'Carries TotDist', 'Carries PrgDist', 'Carries PrgC', 'Carries 1/3', 
                                                         'Carries CPA', 'Carries Mis', 'Carries Dis', 'Receiving Rec','Receiving PrgR']]
        print("FBref EPL squad shooting data downloaded")
    except:
        epl_squad_shooting_for = pd.DataFrame()
        print("No new Fbref squad shooting data acquired")
    # 4 - EPL squad passing stats
    try:
        epl_squad_pass_for = pd.read_html("https://fbref.com/en/comps/9/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"-Premier-League-Stats",
                                                   attrs={"id": "stats_squads_passing_for"})[0]
        epl_squad_pass_for = epl_squad_pass_for[['Squad', 'Total Cmp', 'Total Att', 'Total Cmp%', 'Total PrgDist', 'Short Cmp', 'Short Att', 'Short Cmp%', 'Medium Cmp', 
                                                 'Medium Att', 'Medium Cmp%', 'Long Cmp', 'Long Att', 'Long Cmp%', 'Ast', 'xAG', 'Expected xA', 'KP', '1/3', 'PPA', 'CrsPA', 'PrgP']]
        print("FBref EPL squad passing data downloaded")
    except:
        epl_squad_pass_for = pd.DataFrame()
        print("No new Fbref squad passing data acquired")
    # 5 - EPL squad goal and shot creation stats
    try:
        epl_squad_goal_shot_crt_for = pd.read_html("https://fbref.com/en/comps/9/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"-Premier-League-Stats",
                                                   attrs={"id": "stats_squads_gca_for"})[0]
        epl_squad_goal_shot_crt_for = epl_squad_goal_shot_crt_for[['Squad', 'Standard Gls', 'Standard Sh', 'Standard SoT', 'Standard SoT%', 'Standard Sh/90', 'Standard SoT/90', 
                                                                   'Standard G/Sh', 'Standard G/SoT', 'Standard Dist', 'Standard FK', 'Standard PK', 'Expected xG', 'Expected npxG', 'Expected npxG/Sh']]
        print("FBref EPL squad goal/shot creation data downloaded")
    except:
        epl_squad_goal_shot_crt_for = pd.DataFrame()
        print("No new Fbref squad goal/shot creation data acquired")
    # 6 - EPL squad defensive actions stats
    try:
        epl_def_actns_for = pd.read_html("https://fbref.com/en/comps/9/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"-Premier-League-Stats",
                                         attrs={"id": "stats_squads_defense_for"})[0]
        epl_def_actns_for = epl_def_actns_for[['Squad', 'SCA SCA', 'SCA SCA90', 'SCA Types PassLive', 'SCA Types PassDead', 'SCA Types TO', 'SCA Types Sh', 'SCA Types Fld',
                                               'SCA Types Def', 'GCA GCA', 'GCA GCA90', 'GCA Types PassLive', 'GCA Types PassDead', 'GCA Types TO', 'GCA Types Sh', 'GCA Types Fld', 'GCA Types Def']]
        print("FBref EPL squad defensive actions data downloaded")
    except:
        epl_def_actns_for = pd.DataFrame()
        print("No new Fbref squad defensive actions data acquired")
    # 7 - EPL squad possesion stats
    try: 
        epl_squad_poss_for = pd.read_html("https://fbref.com/en/comps/9/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"-Premier-League-Stats",
                                          attrs={"id": "stats_squads_possession_for"})[0]
        epl_squad_poss_for = epl_squad_poss_for[['Squad', 'Tackles Def 3rd', 'Tackles Mid 3rd', 'Tackles Att 3rd', 'Challenges Tkl%', 'Int', 'Tkl+Int', 'Clr', 'Err']]
        print("FBref EPL team possession data downloaded")
    except:
        epl_squad_poss_for = pd.DataFrame()
        print("No new Fbref overall data acquired")    
    # all tables placed within an array (python list)
    epl_gen_teams_data = [
        epl_overall_for,
        epl_squad_stats_for,
        epl_squad_poss_for,
        epl_squad_pass_for,
        epl_squad_shooting_for,
        epl_squad_goal_shot_crt_for,
        epl_def_actns_for,
    ]
    # Reformatting columns due to multiindex tuple structure when scraped from website 
    for df in epl_gen_teams_data:
        if str(type(df.columns)) == "<class 'pandas.core.indexes.multi.MultiIndex'>":
            new_cols = []
            for col in df.columns:
                if col[0].startswith("Unnamed"):
                    new_cols.append(col[1])
                else:
                    new_cols.append(col[0]+" "+col[1])
            df.columns = new_cols
    return epl_gen_teams_data

