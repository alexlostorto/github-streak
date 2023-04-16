from src.response import contactAPI
from src.streak import getCurrentStreak, getLongestStreak
from src.contributions import getTotalContributions
from src.tables import createTable


def main():
    response = contactAPI()
    currentStreak = getCurrentStreak(response)
    longestStreak = getLongestStreak(response)
    totalContributions = getTotalContributions(response)

    statistics = createTable(currentStreak, longestStreak, totalContributions)
    print(statistics)


if __name__ == '__main__':
    main()
