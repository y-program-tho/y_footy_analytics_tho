import fbref_batch_scraper as fds

epl_data = fds.epl_for_league_data([2025, 2026])

epl_data[4].head(10)