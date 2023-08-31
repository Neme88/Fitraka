# run.py

from Fitraka_Project import create_app
from config import Config  # Import your configuration class

# Use the create_app function to create the Flask app with your configuration class
Fitraka_Project = create_app(Config)

if __name__ == '__main__':
    Fitraka_Project.run(debug=True)

