from contributions import getContributionDays


def getCurrentStreak(response):
    contributions = getContributionDays(response)
    currentStreak = 0

    for day in reversed(contributions):
        if day['contributionCount'] >= 1:
            currentStreak += 1
        else:
            return currentStreak


def getLongestStreak(response):
    contributions = getContributionDays(response)
