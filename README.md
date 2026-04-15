# 🎵 Music Recommender Simulation

## Project Summary

This project builds a small content-based music recommender that ranks songs from `data/songs.csv` based on a user's preferred genre, mood, and energy level. It shows how recommendation systems turn simple song features into personalized suggestions and how different user profiles can produce different results.

---

## How The System Works

This recommender uses a **content-based filtering** approach. For each user profile, it compares every song in the catalog with the user's preferred genre, mood, and target energy.

- **Song features used:** The main scoring logic uses `genre`, `mood`, and `energy` from `data/songs.csv`.
- **User profile information:** The user profile stores the preferred genre, preferred mood, and target energy, for example `{"genre": "pop", "mood": "happy", "energy": 0.8}`.
- **Scoring mechanism:** Each song gets an individual score for genre, mood, and energy. Genre and mood are binary matches, while energy is scored by proximity using `1 - abs(user_preference - song_value)`.
- **Weighted total:** The final score is a weighted average:

  `Total Score = (0.2 * genre_score) + (0.3 * mood_score) + (0.5 * energy_score)`

- **Choosing recommendations:** After scoring the full catalog, the system sorts songs from highest to lowest score and returns the top results for that user.

![alt text](image.png)

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

The starter app tests several different user profiles to show how the rankings change:

- Happy Pop Fan
- Intense Rock Fan
- Chill Lofi Fan
- Peaceful Classical Fan

Those profiles help you compare how the recommender behaves for different tastes and whether the top songs feel consistent with each user's preferences.

---

## Limitations and Risks

The current recommender has a few important limits:

- It only uses a small song catalog, so the recommendation space is limited.
- It only scores three features directly, so it ignores other useful signals like lyrics, artist popularity, or instrumentation.
- The heavy energy weight means the system can favor energy matches even when genre or mood are less aligned.
- The dataset can create bias if some genres or moods are underrepresented.

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned about how recommenders turn data into predictions and where bias or unfairness could show up in systems like this.

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:

- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:

- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:

- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"
```

![alt text](image.png)
