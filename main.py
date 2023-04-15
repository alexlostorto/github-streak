from src.response import contactAPI
from src.streak import getCurrentStreak, getLongestStreak
from src.contributions import getTotalContributions


def main():
    response = contactAPI()
    currentStreak = getCurrentStreak(response)
    longestStreak = getLongestStreak(response)
    totalContributions = getTotalContributions(response)

    print(f"Current streak: {currentStreak}")
    print(f"Longest streak: {longestStreak}")
    print(f"Total contributions: {totalContributions}")


if __name__ == '__main__':
    main()
