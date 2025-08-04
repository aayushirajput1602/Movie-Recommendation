🎬 Movie Recommendation System
This is a content-based Movie Recommendation System built with Python. It suggests similar movies based on user selection by comparing features stored in preprocessed .pkl files.

🚀 Features
Recommend similar movies based on a selected title

Uses precomputed similarity scores for fast results

Flask backend to serve recommendations via a web interface

Designed for deployment on platforms like Render or Heroku

🗂️ Project Structure
bash
Copy
Edit
pycharm/
│
├── app.py                # Main Flask app for serving recommendations
├── movies.pkl            # Pickled DataFrame of movie information
├── movies_dict.pkl       # Pickled dictionary of movie data
├── similarity.pkl        # Precomputed similarity matrix (NOT tracked due to size)
├── requirements.txt      # Python dependencies
├── setup.sh              # Setup script for deployment
├── Procfile              # Used for deploying to Heroku
├── ssl_test.py           # Optional SSL testing script
├── .gitignore            # Ignoring large files and environment-specific configs
📌 Note: similarity.pkl is over 100MB and excluded from the repository using .gitignore.

💻 Getting Started
Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/Movie-Recommendation.git
cd Movie-Recommendation
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
python pycharm/app.py
Access in browser:

cpp
Copy
Edit
http://127.0.0.1:5000
🧠 How It Works
Movie data and similarity scores are preprocessed and stored in .pkl files.

When a movie is selected, the app retrieves the most similar movies using cosine similarity.

The result is returned as a list of recommended titles.
