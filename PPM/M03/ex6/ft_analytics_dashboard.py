"""
This module provides a simple analytics dashboard using Streamlit to
visualize data.
It includes functionalities for loading data, performing basic
analytics, and displaying interactive charts.
"""


def list_exemples():
    """
    Demonstrates various list comprehension examples with a
    list of player data.
    It prints high scorers, doubled scores, and active players.
    """

    print("=== List Comprehension Examples ===\n")
    players_scores = [
        ("alice", 2300, True),
        ("bob", 1800, False),
        ("charlie", 2150, True),
        ("diana", 2050, True),
    ]
    high_scores = [
        players for players, scores, active in players_scores if scores > 2000
    ]
    double_score = [scores * 2 for players, scores, active in players_scores]
    active_players = [
        players for players, scores, active in players_scores if active
        ]
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {double_score}")
    print(f"Active players: {active_players}")


def set_exemples():
    """
    Demonstrates various set comprehension examples with a list of game events.
    It prints unique event types and events from a specific player.
    """
    print("\n=== Set Comprehension Examples ===\n")
    players_name = ["alice", "bob", "charlie", "alice"]
    game_achievements = ["first_blood", "level_up", "first_blood"]
    regions = ["north", "south", "east", "west", "north"]
    unique_players = {players for players in players_name}
    unique_achievements = {achievements for achievements in game_achievements}
    unique_regions = {regions for regions in regions}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Unique regions: {unique_regions}")


def dict_exemples(game_achievement):
    """
    Demonstrates various dictionary comprehension examples with a list of
    player data and event logs.
    It prints player scores as a dictionary, and counts events per player.
    """
    print("\n=== Dictionary Comprehension Examples ===\n")
    game_score_categories = {
        "high": 3,
        "medium": 2,
        "low": 1,
    }
    player_score = {
        player: info["score"] for player, info
        in game_achievement.items()
    }
    score_categories = {
        category: count for category, count in game_score_categories.items()
    }
    achievement_count = {
        player: info["achievement_count"] for player, info
        in game_achievement.items()
    }
    print(f"Player scores: {player_score}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_count}")


def main():
    """
    Main function to run the Streamlit analytics dashboard.
    It sets up the page configuration and calls other functions
    to display content
    """
    game_achievement = {
        "alice": {
            "score": 458,
            "score_categories": 3,
            "achievement_count": 5,
        },
        "bob": {
            "score": 145,
            "score_categories": 2,
            "achievement_count": 3,
        },
        "charlie": {
            "score": 215,
            "score_categories": 1,
            "achievement_count": 2,
        },
    }
    print("=== Game Analytics Dashboard ===\n")
    list_exemples()
    dict_exemples(game_achievement)
    set_exemples()
    print("\n=== Combined Analysis ===")
    print(f"Total Players: {len(game_achievement)}")
    print(
        "Total Events: ",
        sum(info['achievement_count']
            for info in game_achievement.values())
        )
    print(
        "Total Achievements: ",
        sum(info['score_categories']
            for info in game_achievement.values())
        )


if __name__ == "__main__":
    main()
