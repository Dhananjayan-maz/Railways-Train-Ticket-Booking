# 🚆 RailConnect – Train Ticket Booking System (Django)

A full‑featured railway e‑ticketing web application built with Django.  
**Admin‑first design** – All prices, city routes, and per‑km charges are configurable from the Django admin panel without touching a single line of code.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2-green.svg)

---

## ✨ Features

- **User Authentication** – Registration, Login, Password Change, Profile Update (with photo)
- **Ticket Booking** – Select source/destination, travel class, number of passengers → dynamic price calculation
- **Dynamic Pricing** – Fare = `(distance in km) × (per_km_rate)` (per_km_rate can be different for each travel class)
- **Admin Configurable** – Add/Edit cities, set distances between cities, change per‑km price per class – all from Django admin
- **Dashboard** – View booking history, total amount spent, cancel tickets
- **Responsive UI** – Designed with **Indian Railways theme** (blue & orange gradient, modern cards)
- **Secure** – CSRF protection, password hashing, user session management

<img width="1352" height="638" alt="train1" src="https://github.com/user-attachments/assets/ac3fddd2-cdd3-4801-b4ac-b2997f338b3b" />
<img width="1343" height="680" alt="train3" src="https://github.com/user-attachments/assets/69acbc0a-7805-430c-b799-ffcf83e45c48" />
<img width="1361" height="681" alt="train2" src="https://github.com/user-attachments/assets/ea127500-4605-490b-acd4-4725caf5b2a6"/>
---

## 🧠 How Price Calculation Works (No Code Changes Needed)

The system does **not** require you to edit views or models to change fares. Everything is stored in the database and can be modified by an admin user.

1. **City Model** – stores city name.
2. **Route (CityDistance) Model** – stores `(source_city, destination_city, distance_in_km)`.
3. **Class Model** – stores class name (e.g., "AC 3 Tier", "Sleeper") and `price_per_km` for that class.
4. **Booking** – When a user books:
   - System fetches distance between selected cities.
   - Multiplies distance by `price_per_km` of the chosen class.
   - Multiplies by number of tickets → total amount.

👉 **To change a fare**:  
- Go to `/admin` → **CityDistance** → update the km between two cities, **or**  
- Go to **Class** → change `price_per_km` for a class.  
The front‑end booking form will reflect the new price immediately.

No need to touch `views.py`, `urls.py`, or JavaScript.

---

## 📁 Project Structure (Simplified)

Train_Ticket_Booking/

├── manage.py

├── MySQL

├── requirements.txt

├── static/

├── templates/

│ ├── base.html

│ ├── index.html

│ ├── login.html

│ ├── signup.html

│ ├── dashboard.html

│ ├── booking.html

│ ├── change_password.html

│ └── profile_update.html

├── booking_app/

│ ├── models.py # City, CityDistance, TrainClass, Booking

│ ├── admin.py # Register models for admin panel

│ ├── views.py # Booking, dashboard, cancel

│ └── urls.py

└── railconnect/

├── settings.py

└── urls.py
---

# Tech Stack
Backend: Django 5.2
Frontend: HTML, CSS, Bootstrap, AdminLTE
Database: MySQL / SQLite
Language: Python 3.11+

## 🛠️ Setup Instructions (Run Locally)

### Prerequisites
- Python 3.11+
- pip
- Virtual environment (recommended)

### Step 1 – Clone the repository
```bash
git clone https://github.com/Dhananjayan-maz/Railways-Train-Ticket-Booking.git

cd train


### Step 2 – Create virtual environment & install dependencies

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### Step 3 – Apply migrations & create superuser

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   # Follow prompts (admin login for /admin)

` ``` `

### Step 4 – Load initial data (optional)

You can add cities, distances, and classes via the admin panel after running the server.

### Step 5 – Run development server

python manage.py runserver
Visit http://127.0.0.1:8000 – you’re ready!

---

🔧 Admin Panel Usage
Access at: http://127.0.0.1:8000/admin

To add / modify cities:
City → Add city name.

To set distance between two cities:
City Distance → Choose source city, destination city, enter distance (km).

To change fare per class:
Train Class → Edit existing class (e.g., Sleeper) and change Price per Km.

To view bookings:
Booking → See all user bookings.

📬 Contact
For any queries: mdhananjayan581@gmail.com
Project Link: https://github.com/Dhananjayan-maz/Railways-Train-Ticket-Booking.git
