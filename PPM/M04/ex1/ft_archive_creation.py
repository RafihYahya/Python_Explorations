"""
This module handles the creation of archive files.
"""


def main():
    """
    Main function to orchestrate archive creation.
    """
    text_file = "new_discovery.txt"
    data = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee"
    ]
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {text_file}")
    try:
        f = open(text_file, "r",  encoding='utf-8')
        print("Storage unit created successfully...")
        for index, line in enumerate(data):
            out = "{[}ENTRY " + index + "{]}" + line + "\n"
            print(out)
            f.write(out)
        print("Data inscription complete. Storage unit sealed.")
        print(
            f"Archive {text_file}"
            "ready for long-term preservation."
            )
    except OSError as e:
        print("Creation of Archive Failed", e)
        return
    print("Inscribing preservation data...")


if __name__ == "__main__":
    main()
