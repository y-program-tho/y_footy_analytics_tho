import pandas as pd

# Latest EPL league table
#epl_overall_for = pd.read_html("https://fbref.com/en/comps/9/Premier-League-Stats", attrs={"id": "results2025-202691_overall"})[0].set_index("Rk")

# EPL squad standard stats
epl_squad_strd_for = pd.read_html("https://fbref.com/en/comps/9/Premier-League-Stats", attrs={"id": "stats_squads_standard_for"})[0]
epl_squad_strd_for.head(10)

# EPL squad shooting stats
epl_squad_shooting_for = pd.read_html("https://fbref.com/en/comps/9/Premier-League-Stats", attrs={"id": "stats_squads_shooting_for"})[0]
epl_squad_shooting_for.head(10)

# EPL squad passing stats
epl_squad_pass_for = pd.read_html("https://fbref.com/en/comps/9/Premier-League-Stats", attrs={"id": "stats_squads_passing_for"})

# EPL squad goal + shot creation stats
epl_squad_goal_shot_crt_for = pd.read_html("https://fbref.com/en/comps/9/Premier-League-Stats", attrs={"id": "stats_squads_gca_for"})

# EPL squad defensive action stats
epl_def_actns_for = pd.read_html("https://fbref.com/en/comps/9/Premier-League-Stats", attrs={"id": "stats_squads_defense_for"})

# EPL squad possession stats
epl_squad_possession_for = pd.read_html("https://fbref.com/en/comps/9/Premier-League-Stats", attrs={"id": "stats_squads_possession_for"})




