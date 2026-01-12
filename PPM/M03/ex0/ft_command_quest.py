"""This module provides functions related to the command quest game."""
import sys
def main():
    """Entry point for the command quest game."""
    print("=== Command Quest ===")
    arg_len = len(sys.argv)
    if arg_len == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arg_len - 1}")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {arg_len}")
    for i in sys.argv[1:]:
        print(f"Argument {sys.argv.index(i)}: {i}")

if __name__ == "__main__":
    main()
