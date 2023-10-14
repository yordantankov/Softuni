from collections import Counter

if __name__ == "__main__":
    # Read text from the console
    text = input()

    # Convert text to lowercase for case-insensitive counting
    text = text.lower()

    # Count occurrences of each character
    character_counts = Counter(text)

    # Sort the results in alphabetical order
    sorted_counts = sorted(character_counts.items(), key=lambda x: x[0])

    # Print the results
    for char, count in sorted_counts:
        print(f"{char}: {count} time/s")