"""
This module provides a function to respond to various crisis scenarios based on
their severity and type, demonstrating conditional logic and string formatting.
"""


def main():
    """
    Main function to run the crisis response system.
    It prompts the user for crisis details and prints a tailored response.
    """
    print("=== CYBER ARCHIVES- CRISIS RESPONSE SYSTEM ===\n")
    archive01 = "lost_archive.txt"
    archive02 = "classified_vault.txt"
    archive03 = "standard_archive.txt"
    try:
        print(f"CRISIS ALERT: Attempting access to {archive01}...")
        with open(archive01, "r", encoding="utf-8") as archive_file:
            archive_file.read()
    except OSError:
        print("RESPONSE: Archive not found in storage matrix")
    try:
        print(f"CRISIS ALERT: Attempting access to {archive02}...")
        with open(archive02, "r", encoding="utf-8") as archive_file:
            archive_file.read()
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except OSError:
        print("RESPONSE: Archive not found in storage matrix")
    try:
        print(f"ROUTINE ACCESS: Attempting access to {archive03}...")
        with open(archive03, "r", encoding="utf-8") as archive_file:
            archive_file.read()
        print("SUCCESS: Archive recovered- Knowledge preserved for humanity")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except OSError:
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Normal operations resumed")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
