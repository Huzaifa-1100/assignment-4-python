def mad_libs():
    print("Welcome to Mad Libs!\n")
    noun = input("Enter a noun: ").strip()
    verb = input("Enter a verb (e.g., run): ").strip()
    adjective = input("Enter an adjective: ").strip()
    adverb = input("Enter an adverb (e.g., quickly): ").strip()

    story = f"""
    Once upon a time, there was a {adjective} {noun} who loved to {verb}.
    One day, they decided to {verb} {adverb}, and everyone cheered!
    What a {adjective} adventure it was!
    """
    print("\nHere's your Mad Libs story:")
    print(story)


if __name__ == "__main__":
    mad_libs()