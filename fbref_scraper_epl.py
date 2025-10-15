import pandas as pd

epl_overall = pd.read_html("https://fbref.com/en/comps/9/Premier-League-Stats", attrs={"id": "results2025-202691_overall"})[0]#.set_index("Rk", inplace=True)

epl_overall.head(10)


