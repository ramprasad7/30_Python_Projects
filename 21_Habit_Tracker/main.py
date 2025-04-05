import pandas as pd
from tabulate import tabulate
from datetime import datetime
from Habit_Tracker import track_habits, Habit


def main():
    habits: list[Habit] = [
        track_habits('Coffe',datetime(2025, 2,5), cost=1, minutes_used=5),
        track_habits('insta scrolling', datetime(2025,3,30),cost=10, minutes_used=60)
    ]

    df = pd.DataFrame(habits)
    print(tabulate(df, headers="keys",tablefmt="psql"))


if __name__ == '__main__':
    main()