# To contact GitHub's API
import requests

# To authenticate request
from src.credentials import getCredentials


def contactAPI():
    TOKEN, USER = getCredentials()

    URL = 'https://api.github.com/graphql'

    BODY = {
        "query": """query {
            user(login: "<USERNAME>") {
                name
                contributionsCollection {
                    contributionCalendar {
                        totalContributions
                        weeks {
                            contributionDays {
                                color
                                contributionCount
                                date
                                weekday
                            }
                        }
                    }
                }
            }
        }"""
    }

    BODY['query'] = BODY['query'].replace('<USERNAME>', USER)

    HEADERS = {
        'Authorization': f'bearer {TOKEN}'
    }

    response = requests.post(url=URL, json=BODY, headers=HEADERS)

    return response.json()
