def getContributionDays(response):
    weeks = response['data']['user']['contributionsCollection']['contributionCalendar']['weeks']

    contributions = []

    for week in weeks:
        for day in week['contributionDays']:
            contributions.append(day)

    return contributions


def getTotalContributions(response):
    return response['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions']
