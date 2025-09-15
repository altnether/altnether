import pandas as pd

# Mock player data — replace with ESPN API integration later
def get_player_projections():
    data = [
        {"name": "Christian McCaffrey", "position": "RB", "team": "SF", "rostered_pct": 99.9, "stats": {
            "rushing_yards": 85, "rushing_tds": 1, "receiving_yards": 30, "receiving_tds": 0, "fumbles": 0
        }},
        {"name": "Patrick Mahomes", "position": "QB", "team": "KC", "rostered_pct": 100.0, "stats": {
            "passing_yards": 280, "passing_tds": 2, "interceptions": 1, "rushing_yards": 20, "fumbles": 0
        }},
        {"name": "Garrett Wilson", "position": "WR", "team": "NYJ", "rostered_pct": 75.3, "stats": {
            "receiving_yards": 65, "receiving_tds": 1, "fumbles": 0
        }},
        {"name": "Low Roster Guy", "position": "WR", "team": "FA", "rostered_pct": 5.0, "stats": {
            "receiving_yards": 45, "receiving_tds": 0, "fumbles": 1
        }}
    ]

    projections = []
    for player in data:
        stats = player["stats"]
        points = 0

        if "passing_yards" in stats:
            points += stats["passing_yards"] / 25
        if "passing_tds" in stats:
            points += stats["passing_tds"] * 4
        if "interceptions" in stats:
            points -= stats["interceptions"] * 2
        if "rushing_yards" in stats:
            points += stats["rushing_yards"] / 10
        if "rushing_tds" in stats:
            points += stats["rushing_tds"] * 6
        if "receiving_yards" in stats:
            points += stats["receiving_yards"] / 10
        if "receiving_tds" in stats:
            points += stats["receiving_tds"] * 6
        if "fumbles" in stats:
            points -= stats["fumbles"] * 2

        if player["rostered_pct"] >= 20:
            projections.append({
                "name": player["name"],
                "position": player["position"],
                "team": player["team"],
                "rostered_pct": player["rostered_pct"],
                "projected_points": round(points, 2)
            })

    return pd.DataFrame(projections)
