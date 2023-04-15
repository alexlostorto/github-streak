from src.contributions import getContributionDays


def getCurrentStreak(response):
    contributions = getContributionDays(response)
    currentStreak = 0

    if contributions[-1]['contributionCount'] == 0:
        contributions.pop()

    for day in reversed(contributions):
        if day['contributionCount'] >= 1:
            currentStreak += 1
        else:
            return currentStreak

    return currentStreak


def getLongestStreak(response):
    contributions = getContributionDays(response)
    streaks = []
    streak = 0

    for day in reversed(contributions):
        if day['contributionCount'] >= 1:
            streak += 1
        else:
            streaks.append(streak)
            streak = 0

    return max(streaks)
