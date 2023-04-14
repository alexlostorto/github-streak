from response import contactAPI
from streak import getCurrentStreak, getLongestStreak
from contributions import getTotalContributions


def main():
    import json

    response = contactAPI()

    print(getCurrentStreak(response))
    print(getTotalContributions(response))


if __name__ == '__main__':
    main()
