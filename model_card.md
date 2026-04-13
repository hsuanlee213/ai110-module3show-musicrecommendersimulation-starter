# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
**VibeMatch CLI 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  
- 
This recommender is designed to suggest songs based on a user’s preferred genre, mood, energy level, and acoustic preference. It assumes the user can be represented by a small set of simple preferences. This system is intended for classroom exploration, not for real-world deployment.


---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model compares each song in the catalog to a user profile. It uses features such as genre, mood, energy, and acousticness. Songs get points for matching the user’s preferred genre and mood, and they also get a higher score when their energy is closer to the user’s target energy. If the user likes acoustic songs, the model adds a small bonus for songs with stronger acoustic qualities.


---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The model uses a small song catalog stored in `songs.csv`. The dataset contains a limited mix of genres and moods, including pop, lofi, rock, ambient, jazz, and synthwave. I expanded the starter data, but the catalog is still small and does not cover the full range of musical taste. Some genres and moods are represented by only one or two songs.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works best for clear preference profiles such as High-Energy Pop, Chill Lofi, and Deep Intense Rock. It does a good job capturing simple patterns like matching genre and finding songs with similar energy. In several tests, the top recommendations matched my musical intuition.


---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One major weakness is that the system relies too heavily on exact genre matching in a small dataset. If a genre has only one song, that song can dominate the recommendations and create a filter bubble. This means some users get less variety than others, especially when their preferred genre or mood is underrepresented. The model also uses exact labels, so similar categories may be treated as completely different.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested the system with several user profiles, including High-Energy Pop, Chill Lofi, Deep Intense Rock, and an edge-case profile called Acoustic Metal. I checked whether the top results felt reasonable based on genre, mood, and energy. I also ran a small experiment by temporarily removing the mood check to see how the rankings changed. That experiment showed that mood helps the system better capture musical vibe.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I would improve the model by expanding the dataset and adding more variety across genres and moods. I would also like to support softer matching between similar genres or moods instead of exact labels only. Another improvement would be increasing diversity in the top results so the same songs do not appear too often. Better explanations for why a song was recommended would also help.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

This project helped me understand that recommender systems are not just about code, but also about design choices and tradeoffs. A small change in scoring logic can noticeably change the recommendations. I also learned that even a simple music recommender can develop bias when the dataset is small or uneven. It made me think more carefully about how real music apps balance accuracy, variety, and fairness.