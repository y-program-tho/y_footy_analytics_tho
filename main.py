import pandas as pd

szn_yrs = [2025, 2026]

epl_squad_stats_for = pd.read_html("https://fbref.com/en/comps/9/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"/"+str(szn_yrs[0])+"-"+str(szn_yrs[1])+"-Premier-League-Stats",
                                           attrs={"id": "stats_squads_standard_for"})[0]

epl_squad_stats_for.head(10)

cols = epl_squad_stats_for.columns