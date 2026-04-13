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

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Print header
    print("\n" + "=" * 60)
    print("🎵 TOP MUSIC RECOMMENDATIONS 🎵")
    print("=" * 60 + "\n")

    # Print each recommendation with ranking
    for rank, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        
        # Format ranking number
        print(f"#{rank}. {song['title']}")
        print(f"    Artist: {song['artist']}")
        print(f"    Score: {score:.2f}/5.00")
        print(f"    Why: {explanation}")
        print()

    print("=" * 60)



if __name__ == "__main__":
    main()
