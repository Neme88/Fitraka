## Fitraka Fitness Tracking Application.
**Fitraka Fitness Tracking Applicatian** is an all-inclusive fitness management system designed to assist individuals of all fitness levels in achieving their health and fitness objectives.

## Table of contents
- Overview
- Features
- Installation
- Configuration
- Usage
- Dependencies
- Known Issues
- Contributing
- License
- Author

## Overview

Fitraka is an open-source fitness tracking application aimed at helping individuals monitor and enhance their fitness journey. It offers personalized fitness and nutrition management, progress tracking, and community support to motivate users toward achieving their health goals.

## Features
- **Personalized Accounts:** Create an account to access all app features and set personalized goals.
- **Fitness Goal Tracking:** Track fitness objectives like weight loss, muscle gain, or overall fitness improvement.
- **Workout Logging:** Log daily routines, including exercises, sets, reps, and weights.
- **Nutrition Management:** Track caloric intake and maintain a food journal to manage your nutrition.
- **Community Support:** Engage with a community of fitness enthusiasts for motivation and advice.
- **Progress Reports:** View comprehensive reports and statistics to track and assess your progress over time.
## Installation
### Prerequisites
Ensure the following prerequisites are met:
- **Python** 3.8 or higher is installed.
- **pip,** the Python package manager, is available.

## Installation Steps

  1. ### Clone the repository:

    git clone https://github.com/Neme88/Fitraka.git
    
  2. ### Navigate to the project directory:
    cd Fitraka

  3. ### Create a virtual Development environment:
     Create a virtual Development environment to isolate your current project repo from other repos and directories in you local machine that way your dependecies will solely be for the project.and it helps avoid clutter.
     
        virtual venv

  4. ### Activate the virtual environment:
  
  - on windows OS.
        
        venv\Scripts\activate

  - On macOS/Linux
      
        source venv/bin/activate
  
5. ### Install required dependencies:
        
        pip install -r requirements.txt

## Configuration

### Database Setup

To configure the database, run the following commands:
        
    flask db init
    flask db migrate
    flask db upgrade

### Usage

Start the application locally by executing
        
    flask run

Once the server is running, you can access the application by navigating to http://localhost:5000 in your browswe.

### Dependencies

The Fitraka Fitness Tracking Application relies on the following Python packages:

- charset-normalizer==2.0.12
- click==8.1.7
- contourpy==1.1.0
- cycler==0.11.0
- dominate==2.8.0
- Flask==2.0.1
- Flask-Cors==4.0.0
- Flask-Login==0.6.0
- Flask-Mail==0.9.1
- Flask-Migrate==3.1.0
- Flask-MySQLdb==0.2.0
- Flask-RESTful==0.3.9
- Flask-SQLAlchemy==2.5.1
- Flask-Uploads==0.2.1
- Flask-WTF==0.15.1

### Known Issues
- Users may encounter issues with the database migration on certain setups.
- Some users have reported intermittent issues with session management when using the Flask-Login module.

### Contributing

We welcome contributions from the community to improve the application. To contribute:

- Fork the repository.
- Create a new branch for your feature or fix.
- Submit a pull request with a detailed explanation of your changes.

Please make sure your contributions align with the project's overall goals.

### License

This project is open-source and available under the MIT License. See the LICENSE file for more information.

### Author
**Chinemerem .C.Nwaka**
**Email: ccnwaka1988@gmail.com**
**Linkedin: https://www.linkedin.com/in/chinemerem-c-nwaka/**
**GitHub: https://github.com/Neme88**

