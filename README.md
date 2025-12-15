# Wishbox

Wishbox is a Django-based e-commerce web application for browsing, customizing, and purchasing gifts and products. It features user accounts, product management, shopping cart functionality, and integration with MongoDB for custom orders.

## Features

- User authentication and profiles
- Product catalog with customization options
- Shopping cart and checkout
- Contact forms and newsletters
- Responsive design with static assets (CSS/JS)
- SQLite for main data, MongoDB for custom order storage

## Prerequisites

- Python 3.12+
- Docker and Docker Compose (for containerized setup)
- MongoDB (if running locally without Docker)

## Installation

1. Clone the repository:
   `
   git clone https://github.com/yourusername/wishbox.git
   cd wishbox
   `

2. Create a virtual environment:
   `
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   `

3. Install dependencies:
   `
   pip install -r requirements.txt
   `

4. Set up environment variables:
   - Create a .env file in the root directory (copy from .env if it exists).
   - Ensure SECRET_KEY, MONGO_URL, and MONGO_DB_NAME are set.

5. Run migrations:
   `
   python manage.py migrate
   `

6. Collect static files:
   `
   python manage.py collectstatic --noinput
   `

7. Run the development server:
   `
   python manage.py runserver
   `
   Access at http://localhost:8000

## Running with Docker

1. Ensure Docker and Docker Compose are installed.

2. Build and run the services:
   `
   docker-compose up --build
   `
   - The app runs on http://localhost:8000
   - MongoDB runs on localhost:27017 (accessible from the app)

3. Stop the services:
   `
   docker-compose down
   `

## Project Structure

- wishbox/: Django project settings and URLs
- home/: Home page, contact, FAQ, etc.
- ccount/: User authentication and profiles
- shop/: Product catalog, cart, checkout, customization
- static/: CSS, JS, and assets
- 	emplates/: HTML templates
- db.sqlite3: SQLite database
- db_connection.py: MongoDB connection utilities

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make changes and test.
4. Submit a pull request.

## License

This project is licensed under the MIT License.
