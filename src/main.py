"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs, UserProfile


def profile_to_prefs(profile: UserProfile) -> dict:
    """Convert a UserProfile object to the preferences dict format."""
    return {
        "genre": profile.favorite_genre,
        "mood": profile.favorite_mood,
        "energy": profile.target_energy,
        "likes_acoustic": profile.likes_acoustic
    }


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Define multiple user profiles
    profiles = {
        "High-Energy Pop": UserProfile(
            favorite_genre="pop",
            favorite_mood="happy",
            target_energy=0.85,
            likes_acoustic=False
        ),
        "Chill Lofi": UserProfile(
            favorite_genre="lofi",
            favorite_mood="chill",
            target_energy=0.25,
            likes_acoustic=True
        ),
        "Deep Intense Rock": UserProfile(
            favorite_genre="rock",
            favorite_mood="intense",
            target_energy=0.90,
            likes_acoustic=False
        ),
        "Acoustic Metal": UserProfile(
            favorite_genre="rock",
            favorite_mood="intense",
            target_energy=0.95,
            likes_acoustic=True
        )
    }

    # Test each profile
    for profile_name, profile in profiles.items():
        user_prefs = profile_to_prefs(profile)
        recommendations = recommend_songs(user_prefs, songs, k=5)

        # Print profile header
        print("\n" + "=" * 70)
        print(f"👤 {profile_name.upper()}")
        print("=" * 70)
        print(f"Genre: {profile.favorite_genre} | Mood: {profile.favorite_mood} | " +
              f"Energy: {profile.target_energy:.1%} | Acoustic: {profile.likes_acoustic}\n")

        # Print header for recommendations
        print("🎵 TOP 5 RECOMMENDATIONS:\n")

        # Print each recommendation with ranking
        for rank, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            
            print(f"  #{rank}. {song['title']}")
            print(f"      Artist:  {song['artist']}")
            print(f"      Score:   {score:.2f} points")
            print(f"      Reasons: {explanation}")
            print()

    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
