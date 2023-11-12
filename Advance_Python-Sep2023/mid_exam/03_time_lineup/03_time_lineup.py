def team_lineup(*players):
    country_count = {}
    for player in players:
        country = player[1]
        if country in country_count:
            country_count[country].append(player[0])
        else:
            country_count[country] = [player[0]]

    sorted_countries = sorted(country_count.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []
    for country, players in sorted_countries:
        result.append(f"{country}:")
        for player_name in players:
            result.append(f"  -{player_name}")

    return '\n'.join(result)

# Example usage
print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
