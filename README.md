# 🚆 RailConnect – Train Ticket Booking System

A full-featured railway e-ticket booking web application developed using Django that enables users to search routes, calculate dynamic ticket pricing, and manage railway bookings through a secure and responsive dashboard.

The system follows an admin-first architecture where cities, routes, distances, and pricing configurations can be fully managed through the Django admin panel without modifying application code.

---

## 📌 Project Overview

RailConnect is designed to simulate a real-world railway reservation platform with dynamic pricing and configurable route management.

The application allows users to register, book train tickets, manage profiles, and track booking history while administrators can configure routes, fare structures, and travel classes directly from the admin panel.

The pricing engine calculates ticket fares dynamically based on travel distance and class-specific per-kilometer pricing.

---

## ✨ Key Features

### 🔹 User Authentication
- User Registration and Login
- Secure password hashing
- Password change functionality
- Profile management with photo upload
- Session-based authentication

### 🔹 Ticket Booking System
- Select source and destination cities
- Choose travel class
- Dynamic fare calculation
- Multi-passenger ticket booking
- Instant booking confirmation

### 🔹 Dynamic Pricing Engine
- Distance-based fare calculation
- Class-wise configurable pricing
- Real-time total amount generation
- Fully admin-controlled fare structure

### 🔹 Admin Panel Configuration
- Manage cities and routes
- Configure distance between cities
- Modify class-wise price per kilometer
- Monitor user bookings
- No code changes required for pricing updates

### 🔹 Dashboard & Booking Management
- User booking history
- Total ticket spending overview
- Cancel booked tickets
- Booking management interface

### 🔹 UI & User Experience
- Responsive railway-themed UI
- Modern dashboard layout
- Interactive booking workflow
- Indian Railways inspired design

---

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- Bootstrap
- AdminLTE
- JavaScript

### Backend
- Django
- Python

### Database
- MySQL / SQLite

### Development Tools
- VS Code
- GitHub

---

## ⚙️ Ticket Booking Workflow

```text
User Login / Registration
            ↓
Select Source & Destination
            ↓
Choose Travel Class
            ↓
Enter Passenger Count
            ↓
Fetch Distance Between Cities
            ↓
Calculate Fare Dynamically
            ↓
Generate Booking Record
            ↓
Display Booking Confirmation
```

---

## 🧠 Dynamic Pricing Logic

The fare calculation system is fully database-driven and configurable through the admin panel.

### Pricing Formula

```text
Total Fare = Distance × Price Per KM × Number of Passengers
```

### Database Models Used

#### City Model
Stores city names.

#### Route / CityDistance Model
Stores:
- Source city
- Destination city
- Distance in kilometers

#### TrainClass Model
Stores:
- Class name
- Price per kilometer

#### Booking Model
Stores:
- Passenger details
- Booking information
- Total calculated amount

---

## 🧠 Project Architecture

```text
                ┌─────────────────┐
                │ User Interface  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Django Backend  │
                └────────┬────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼                               ▼
┌─────────────────┐           ┌─────────────────┐
│ Authentication  │           │ Pricing Engine  │
│ System          │           │ Booking Logic   │
└────────┬────────┘           └────────┬────────┘
         │                               │
         ▼                               ▼
┌─────────────────────────────────────────────┐
│              MySQL Database                 │
└─────────────────────────────────────────────┘
```

---

## 📸 Project Screenshots

### 🏠 Home Page
<img width="1352" height="638" alt="train1" src="https://github.com/user-attachments/assets/ac3fddd2-cdd3-4801-b4ac-b2997f338b3b" />

### 🎫 Ticket Booking
<img width="1343" height="680" alt="train3" src="https://github.com/user-attachments/assets/69acbc0a-7805-430c-b799-ffcf83e45c48" />

### 📊 User Dashboard
<img width="1361" height="681" alt="train2" src="https://github.com/user-attachments/assets/ea127500-4605-490b-acd4-4725caf5b2a6"/>

---

## 📂 Project Structure

```text
Train_Ticket_Booking/

├── manage.py
├── requirements.txt
├── static/
├── templates/
│
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── booking.html
│   ├── change_password.html
│   └── profile_update.html
│
├── booking_app/
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   └── urls.py
│
└── railconnect/
    ├── settings.py
    └── urls.py
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Dhananjayan-maz/Railways-Train-Ticket-Booking.git

cd Railways-Train-Ticket-Booking
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / macOS
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

---

## 🔧 Admin Panel Usage

Access admin panel:

```text
http://127.0.0.1:8000/admin
```

### Configure Cities
- Add city names
- Manage available routes

### Configure Distances
- Set distance between cities
- Update travel routes dynamically

### Configure Fare Pricing
- Modify price per kilometer
- Manage travel classes

### Manage Bookings
- View user reservations
- Track ticket bookings

---

## 🔒 Security Features

- Password hashing using Django Authentication
- CSRF protection enabled
- Secure session handling
- ORM-based database operations

---

## 🔮 Future Enhancements

- Online payment gateway integration
- Live train availability
- Seat selection system
- Ticket PDF generation
- Email and SMS notifications
- Real-time train tracking
