QueryDesk: Audience Query Management System

QueryDesk is a full-stack web application built in Python and Django. It provides a unified system for brands to manage all incoming audience queries, inspired by a real-world problem statement for customer support.

This system centralizes all audience messages, auto-tags them, allows admins to route and resolve issues, and provides a clean, modern interface for both users and administrators.

Live Demo URL: https://querydesk-live.onrender.com/


Key Features

User Features

User Authentication: Secure user registration (with email), login, and logout.

Modern UI: A clean, responsive, and animated homepage inspired by the Redtape.com aesthetic, featuring on-scroll animations.

Professional Forms: All forms use modern "floating label" animations for a better user experience.

User Dashboard: A personal dashboard where users can view and update their profile information (mobile number, address, etc.).

"My Queries" Page:

Submit Queries: Users can submit new queries (questions, complaints, requests) through an easy-to-use form.

View History: Users can see a complete, filterable history of all their past queries.

Track Status: Queries are clearly marked with their current status (Open, In Progress, Resolved).

View Resolutions: Users can see the final resolution provided by an admin directly on their query card.

Admin & Backend Features

Unified Inbox (Django Admin): The powerful Django Admin panel is customized to serve as a complete "Unified Inbox" for all staff.

Triage & Routing: Admins can view all queries from all users and directly change a query's Status, Priority, and Assign it to other staff members.

Simple Auto-Tagging: New queries are automatically categorized on creation based on keywords in the description (e.g., "refund" is tagged as "Complaint").

Provide Resolutions: Admins have a dedicated "Admin Resolution" field to write a response. This response is then displayed to the user on their "My Queries" page.

Automatic User Profiles: A Profile model is automatically created for every new user upon registration using Django signals.

Tech Stack

Backend: Python, Django

Frontend: HTML, CSS (with modern animations), JavaScript

Database: PostgreSQL (on Render) / SQLite3 (for local development)

Server: Gunicorn

Deployment: Render

The Original Problem Statement

This project was built to solve the following challenge:

"Brands receive thousands of messages across email, social media, chat, and community platforms. Many are lost or delayed, leading to dissatisfied customers and missed opportunities.

Your Challenge: Build a unified system that centralizes all incoming audience queries, categorizes and prioritizes them automatically, routes urgent issues to the right teams, and tracks progress."

How to Run This Project Locally

Clone the repository:

git clone [https://github.com/bhardwajaavi/querydesk-project.git](https://github.com/bhardwajaavi/querydesk-project.git)
cd querydesk-project


Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run database migrations:

python manage.py migrate


Create a local admin user:

python manage.py createsuperuser


Run the development server:

python manage.py runserver


Open http://127.0.0.1:8000/ in your browser.

Created By

Aavi Bhardwaj
