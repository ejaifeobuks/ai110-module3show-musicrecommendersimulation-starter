"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # A list of different user taste profiles to test
    profiles_to_test = [
        {"name": "Happy Pop Fan", "prefs": {"genre": "pop", "mood": "happy", "energy": 0.8}},
        {"name": "Intense Rock Fan", "prefs": {"genre": "rock", "mood": "intense", "energy": 0.9}},
        {"name": "Chill Lofi Fan", "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.4}},
        {"name": "Peaceful Classical Fan", "prefs": {"genre": "classical", "mood": "peaceful", "energy": 0.2}}
    ]

    # --- Loop through each profile and get recommendations ---
    for profile in profiles_to_test:
        user_name = profile["name"]
        user_prefs = profile["prefs"]

        recommendations = recommend_songs(user_prefs, songs, k=3)

        print(f"\n--- Recommendations for: {user_name} ---")
        print(f"Profile: {user_prefs}\n")

        if not recommendations:
            print("  No recommendations found for this profile.")
            continue

        for i, (song, score, explanation) in enumerate(recommendations):
            print(f"  {i+1}. \"{song['title']}\" by {song['artist']}")
            print(f"     Score: {score:.2f}")
            print(f"     Reason: {explanation}\n")


if __name__ == "__main__":
    main()
