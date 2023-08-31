# run.py

from Fitraka import create_app
from config import Config  # Import your configuration class

# Use the create_app function to create the Flask app with your configuration class
Fitraka = create_app()

if __name__ == '__main__':
    Fitraka.run(debug=True)

