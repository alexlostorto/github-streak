from response import contactAPI
from streak import getCurrentStreak, getLongestStreak
from contributions import getTotalContributions


def main():
    import json

    response = contactAPI()
    currentStreak = getCurrentStreak(response)
    totalContributions = getTotalContributions(response)

    print(f"Current streak: {currentStreak}")
    print(f"Total contributions: {totalContributions}")


if __name__ == '__main__':
    main()
