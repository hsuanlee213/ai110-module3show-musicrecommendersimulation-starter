from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs most similar to the user's preferences."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable explanation of why a song was recommended."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    
    songs = []
    print(f"Loading songs from {csv_path}...")
    
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numeric columns to appropriate types
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            
            songs.append(row)
    
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song based on user preferences.
    
    Args:
        user_prefs: Dictionary with keys: genre, mood, energy, likes_acoustic
        song: Dictionary with keys: title, genre, mood, energy, acousticness (and others)
    
    Returns:
        (total_score, reasons) - tuple of float score and list of explanation strings
    """
    score = 0.0
    reasons = []
    
    # Genre match: worth 2.0 points
    if song['genre'] == user_prefs['genre']:
        score += 2.0
        reasons.append("genre match (+2.0)")
    
    # Mood match: worth 1.0 point
    if song['mood'] == user_prefs['mood']:
        score += 1.0
        reasons.append("mood match (+1.0)")
    
    # Energy similarity: based on distance from target energy
    energy_diff = abs(song['energy'] - user_prefs['energy'])
    energy_score = max(0.0, 1.0 - energy_diff)
    score += energy_score
    reasons.append(f"energy close to target (+{energy_score:.2f})")
    
    # Acoustic preference bonus
    if user_prefs.get('likes_acoustic', False) and song['acousticness'] >= 0.5:
        acoustic_bonus = 0.5
        score += acoustic_bonus
        reasons.append(f"acoustic preference match (+{acoustic_bonus})")
    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # Score all songs
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = " | ".join(reasons)  # Convert reasons list to string
        scored_songs.append((song, score, explanation))
    
    # Sort by score (highest first)
    ranked_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)
    
    # Return top-k recommendations
    return ranked_songs[:k]
