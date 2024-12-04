Simon Game 🎵


Overview
Simon Game is a memory-based game that challenges players to repeat an ever-growing sequence of lights and sounds. The goal is to test and improve memory skills while having fun!

Features
Interactive Gameplay: Watch the sequence of lights and sounds and repeat them in the correct order.
Increasing Difficulty: The sequence grows longer with each level.
Audio Feedback: Enjoy distinct tones for each color.
Responsive Design: Play seamlessly on both desktop and mobile devices.
Technologies Used
HTML: For the game’s structure.
CSS: For styling the interface.
JavaScript: To handle game logic and interactions.
How to Play
Start the game by pressing any key or a dedicated Start button.
Observe the sequence of colors and sounds.
Repeat the sequence by clicking on the corresponding buttons in the correct order.
Advance to the next level if the sequence is correct; the game ends if you make a mistake.
Project Structure
bash
Copy code
simon-game/  
│  
├── index.html       # HTML structure  
├── style.css        # Styling for the game  
├── game.js          # Game logic and interactivity  
└── README.md        # Project documentation  
How to Run Locally
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/simon-game.git  
cd simon-game  
Open the index.html file in your preferred web browser.

Play the game and enjoy!

Future Enhancements
Add a high-score tracker to save the best performance.
Introduce custom themes for colors and sounds.
Include multiplayer mode for competitive play.

## Overview
This project is a web application built using Flask and Neo4j. The application allows users to upload CSV files containing candidate information, which is then stored in a Neo4j graph database. The web interface displays the candidate data and provides functionalities such as searching for candidates by name or skills, and clearing the displayed data.

## Features
- **CSV Upload**: Upload candidate data via CSV files.
- **Neo4j Integration**: Store and retrieve candidate, college, degree, and skill information in a Neo4j graph database.
- **Search Functionality**: Search candidates based on name or skills.
- **Dynamic Table**: Display candidate data in a table with the ability to clear data.
- **Relationships**: Models relationships such as `Studied_at`, `Passed_Out`, `Has_degree`, and `Has_skill`.

## Technologies Used
- **Flask**: Python web framework.
- **Neo4j**: Graph database for storing candidate data and relationships.
- **Pandas**: For parsing and handling CSV files.
- **HTML/CSS/JavaScript**: For the frontend.

## Prerequisites
Make sure you have the following installed:
- Python 3.x
- Flask
- Pandas
- Neo4j
- Neo4j Python Driver

You also need to have Neo4j installed and running. You can download it from the [official website](https://neo4j.com/download/).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/flask-neo4j-candidate-uploader.git
    cd flask-neo4j-candidate-uploader
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```

   - **On Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **On macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. Install required dependencies:
    ```bash
    pip install Flask pandas neo4j
    ```

4. Make sure Neo4j is running. Configure your connection details (URI, username, password) in `app.py`:
    ```python
    neo4j_uri = "bolt://localhost:7687"
    neo4j_user = "neo4j" 
    neo4j_password = "your_password"
    ```

5. Run the Flask application:
    ```bash
    flask run
    ```

6. Open your browser and navigate to:
    ```
    http://127.0.0.1:5001/
    ```

## Project Structure
```bash
flask-neo4j-candidate-uploader/
│
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # HTML template for the web interface
├── static/
│   └── style.css          # CSS file (if any)
├── README.md              # This readme file
└── venv/                  # Virtual environment directory
