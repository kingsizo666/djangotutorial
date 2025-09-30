# Django Tutorial Polls App

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.2+-green.svg)](https://www.djangoproject.com/)

A simple polls application built with Django as part of the official Django tutorial. This project demonstrates the basics of Django web development, including models, views, templates, and handling user input.

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- List available polls
- Vote on poll choices
- View real-time poll results
- Responsive design with basic styling

## Installation
```bash
git clone https://github.com/kingsizo666/djangotutorial.git
cd djangotutorial/mysite
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

pip install django
python manage.py migrate
python manage.py runserver
```

## Usage
Open your browser and navigate to `http://127.0.0.1:8000/polls/` to explore the polls application. Select a poll, vote for your favorite option, and view the results.

## Project Structure
```
mysite/
├── manage.py
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   └── urls.py
└── polls/
    ├── migrations/
    ├── templates/
    ├── static/
    ├── admin.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```