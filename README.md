# AI-Driven Health Chatbot

## Overview
The AI-Driven Health Chatbot is an innovative application designed to enhance healthcare accessibility by providing users with a virtual health assistant. This project combines the power of AI with a user-friendly interface to facilitate health-related conversations, manage appointments, and offer administrative functionalities. It aims to solve the problem of limited access to immediate healthcare advice and appointment scheduling, particularly benefiting individuals seeking quick and reliable health consultations. The chatbot can simulate health dialogues, help users manage their appointments, and provide an administrative dashboard for user and appointment management.

## Features
- **AI-Powered Chat Interface**: Engage with an AI chatbot that simulates health-related conversations, providing users with instant responses and guidance.
- **Appointment Management**: Users can view and schedule appointments directly through the application, ensuring seamless healthcare planning.
- **User Authentication**: Secure login functionality for users to access personalized features and manage their profiles.
- **Admin Dashboard**: A dedicated section for administrators to manage users and appointments, ensuring efficient system oversight.
- **Responsive Design**: The application is designed to be responsive, providing a seamless experience across various devices.
- **Static and Dynamic Content**: Combines static HTML pages with dynamic content loading for an interactive user experience.
- **Data Persistence**: Utilizes a SQLite database to store user, appointment, and chat data, ensuring data persistence and retrieval.

## Tech Stack
| Technology   | Description                                      |
|--------------|--------------------------------------------------|
| Python       | Programming language used for backend logic      |
| FastAPI      | Web framework for building APIs                  |
| Uvicorn      | ASGI server for running FastAPI applications     |
| SQLAlchemy   | ORM for database interaction                     |
| Passlib      | Library for password hashing                     |
| SQLite       | Lightweight database for data storage            |
| HTML/CSS/JS  | Frontend technologies for UI/UX                  |

## Architecture
The project is structured with a FastAPI backend serving HTML templates as the frontend. The backend handles API requests, manages database interactions, and serves static files. The frontend consists of HTML templates styled with CSS and enhanced with JavaScript for dynamic behavior.

```plaintext
+-----------------+
|  Frontend       |
|  (HTML/CSS/JS)  |
+-----------------+
        |
        v
+-----------------+
|  FastAPI        |
|  (Backend)      |
+-----------------+
        |
        v
+-----------------+
|  SQLite DB      |
|  (Data Storage) |
+-----------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-driven-health-chatbot-auto.git
   cd ai-driven-health-chatbot-auto
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
Start the application using Uvicorn:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
Visit `http://localhost:8000` in your web browser to access the application.

## API Endpoints
| Method | Path               | Description                              |
|--------|--------------------|------------------------------------------|
| GET    | /                  | Home page                                |
| GET    | /chat              | Chat interface                           |
| GET    | /appointments      | View appointments                        |
| GET    | /login             | User login page                          |
| GET    | /admin             | Admin dashboard                          |
| POST   | /api/chat          | Chat with the AI chatbot                 |
| GET    | /api/appointments  | Retrieve all appointments                |
| POST   | /api/appointments  | Create a new appointment                 |
| POST   | /api/login         | Authenticate user                        |
| GET    | /api/users         | Retrieve all users                       |

## Project Structure
```
.
├── Dockerfile               # Docker configuration file
├── app.py                   # Main application file with FastAPI setup
├── requirements.txt         # Python dependencies
├── start.sh                 # Shell script to start the application
├── static
│   ├── css
│   │   └── style.css        # Stylesheet for frontend
│   └── js
│       └── main.js          # JavaScript for dynamic frontend behavior
└── templates
    ├── admin.html           # Admin dashboard template
    ├── appointments.html    # Appointments page template
    ├── chat.html            # Chat interface template
    ├── index.html           # Home page template
    └── login.html           # Login page template
```

## Screenshots
*Screenshots of the application interface will be added here.*

## Docker Deployment
Build and run the application using Docker:
```bash
docker build -t ai-driven-health-chatbot .
docker run -p 8000:8000 ai-driven-health-chatbot
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push to your branch.
5. Create a pull request.

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.