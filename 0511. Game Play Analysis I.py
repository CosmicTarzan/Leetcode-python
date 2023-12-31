import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by='event_date', inplace=True)
    return activity.drop_duplicates(subset='player_id')[['player_id', 'event_date']].rename(columns={'event_date': 'first_login'})
