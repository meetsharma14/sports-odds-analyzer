def find_best_odds(match):
    best_odds = {}

    for bookmaker in match['bookmakers']:
        for outcome in bookmaker['markets'][0]['outcomes']:

            team = outcome['name']
            price = outcome['price']

            if team not in best_odds or price > best_odds[team]:
                best_odds[team] = price

    return best_odds


def check_arbitrage(best_odds):

    total = 0

    for odd in best_odds.values():
        total += 1 / odd

    return total < 1