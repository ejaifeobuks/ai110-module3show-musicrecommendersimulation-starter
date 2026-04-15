from typing import List, Dict, Tuple, Optional
import csv
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
        """Store the songs available for recommendation."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Tuple[Song, float, str]]:
        """Rank songs for a user and return the top matches with explanations."""
        # Define the weights for each feature
        weights = {
            "genre": 0.2,
            "mood": 0.3,
            "energy": 0.5
        }

        scored_songs = []

        for song in self.songs:
            # Calculate individual feature scores
            genre_score = 1.0 if song.genre == user.favorite_genre else 0.0
            mood_score = 1.0 if song.mood == user.favorite_mood else 0.0
            energy_score = 1 - abs(user.target_energy - song.energy)

            # Calculate the total weighted score
            total_score = (
                weights["genre"] * genre_score +
                weights["mood"] * mood_score +
                weights["energy"] * energy_score
            )
            scored_songs.append((song, total_score))

        # Sort songs by score in descending order
        scored_songs.sort(key=lambda x: x[1], reverse=True)

        # Get top k songs and generate explanations for them
        top_k_songs = scored_songs[:k]
        
        recommendations_with_explanations = []
        for song, score in top_k_songs:
            explanation = self.explain_recommendation(user, song)
            recommendations_with_explanations.append((song, score, explanation))
            
        return recommendations_with_explanations

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song matches a user's preferences."""
        reasons = []
        
        # Check for genre match
        if song.genre == user.favorite_genre:
            reasons.append(f"it's in the '{song.genre}' genre you like")

        # Check for mood match
        if song.mood == user.favorite_mood:
            reasons.append(f"it has the '{song.mood}' mood you're looking for")

        # Describe the energy level
        energy_diff = abs(user.target_energy - song.energy)
        if energy_diff < 0.1:
            reasons.append("it has a very similar energy level")
        elif energy_diff < 0.2:
            reasons.append("it has a similar energy level")

        # Construct the final sentence
        if not reasons:
            return "It's a potential match based on a combination of factors."
        
        explanation = "Because " + " and ".join(reasons) + "."
        return explanation.capitalize()

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    songs = []
    with open(csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert numerical strings to float, except for 'id' which can be int
            try:
                row['id'] = int(row['id'])
                row['energy'] = float(row['energy'])
                row['tempo_bpm'] = float(row['tempo_bpm'])
                row['valence'] = float(row['valence'])
                row['danceability'] = float(row['danceability'])
                row['acousticness'] = float(row['acousticness'])
                songs.append(row)
            except (ValueError, KeyError) as e:
                print(f"Skipping row due to error: {e} in row {row}")
    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Convert raw data into objects, score songs, and return formatted recommendations."""
    # 1. Convert the raw song dictionaries into Song objects
    song_objects = [Song(**s) for s in songs]

    # 2. Convert the user preferences dictionary into a UserProfile object
    # Note: This assumes the keys in user_prefs match the UserProfile fields,
    # which might not be the case. We'll adapt for the 'likes_acoustic' field.
    user_profile = UserProfile(
        favorite_genre=user_prefs.get("genre", ""),
        favorite_mood=user_prefs.get("mood", ""),
        target_energy=user_prefs.get("energy", 0.5),
        likes_acoustic=user_prefs.get("likes_acoustic", False) # Defaulting to False
    )

    # 3. Instantiate the Recommender and get recommendations
    recommender = Recommender(song_objects)
    recommendations = recommender.recommend(user_profile, k)

    # 4. Convert the results back to the required format (Dict, float, str)
    # The dataclasses.asdict helper can be useful here if imported.
    final_results = []
    for song_obj, score, explanation in recommendations:
        song_dict = {
            'id': song_obj.id, 'title': song_obj.title, 'artist': song_obj.artist,
            'genre': song_obj.genre, 'mood': song_obj.mood, 'energy': song_obj.energy,
            'tempo_bpm': song_obj.tempo_bpm, 'valence': song_obj.valence,
            'danceability': song_obj.danceability, 'acousticness': song_obj.acousticness
        }
        final_results.append((song_dict, score, explanation))
        
    return final_results
