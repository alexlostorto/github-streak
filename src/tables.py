# Pretty tables
from src.lib.prettytables import PrettyTable


def createTable(currentStreak, longestStreak, totalContributions):
    table = PrettyTable(['Category', 'Count'], padding=1, separator='curvy')
    table.add_row(['Current Streak', f'{currentStreak} days'])
    table.add_row(['Longest Streak', f'{longestStreak} days'])
    table.add_row(['Total Contributions', f'{totalContributions}'])

    return table
