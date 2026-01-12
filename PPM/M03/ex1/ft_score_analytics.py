"""This module provides functions for analyzing ft_score data."""
import sys


def main():
    """Entry point for the ft_score analytics script."""
    print("=== Player Score Analytics ===")
    argv = sys.argv()
    score_list = []
    if argv == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    try:
        for score in argv[1:]:
            score_list.append(int(score))
        print(f"Total players: {len(score_list)}")
        print(f"Total score: {sum(score_list)}")
        print(f"Average score: {sum(score_list) / len(score_list)}")
        print(f"High score: {max(score_list)}")
        print(f"Low score: {min(score_list)}")
        print(f"Score range: {max(score_list)}")
    except ValueError:
        print(f"oops, You typed {score} instead of 1000")
