# Django  Online Movie Ticket Booking System

This is a Django project for managing movie ticket booking.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [API Endpoints](#api-endpoints)
5. [Models](#models)

## Overview

The Django Ticket Booking System is a web application that allows users to browse available movies, theaters, showtimes, and make reservations and purchases for movie tickets.

## Installation

To run the Django Ticket Booking System locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/AarugulaVarahalu/Online-Movie-Ticket-Booking.git

cd ticket-booking

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

Open your web browser and visit http://127.0.0.1:8000 to access the application.


Usage
Once the application is running, users can perform the following actions:

Register a new account.
Log in to an existing account.
Browse available movies, theaters, and showtimes.
Make reservations and purchases for movie tickets.
Log out from the account.


API Endpoints
The Django Ticket Booking System provides the following API endpoints:

/register/: Register a new user account.
/login/: Log in to an existing user account.
/logout/: Log out from the user account.
/movies/: List all movies and create a new movie.
/movies/<pk>/: Retrieve, update, or delete a specific movie.
/theaters/: List all theaters and create a new theater.
/theaters/<pk>/: Retrieve, update, or delete a specific theater.
/showtime/: List all showtimes and create a new showtime.
/showtime/<pk>/: Retrieve, update, or delete a specific showtime.
/reserve/: List all reservations and create a new reservation.
/reserve/<pk>/: Retrieve, update, or delete a specific reservation.
/purchase/: List all purchases and create a new purchase.
/purchase/<pk>/: Retrieve, update, or delete a specific purchase.



Models
The Django Ticket Booking System includes the following models:

Movie: Represents a movie with title, director, genre, release date, duration, and synopsis.
Theater: Represents a theater with name, location, and capacity.
Showtime: Represents a showtime for a movie at a theater with date and time and available seats.
Reserve: Represents a reservation for a movie at a theater for a specific showtime.
Purchase: Represents a purchase of movie tickets for a specific reservation.
