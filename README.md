# Eshop Project

This is an e-commerce project built with Django. It provides a platform for users to register, login, browse products, add products to their favorites, and contact the site administrators.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ErfanShokrollahzadeh/eshop_project.git
   ```
2. Navigate to the project directory:
   ```
   cd eshop_project
   ```
3. Create a virtual environment:
   ```
   python -m venv myenv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source myenv/bin/activate
     ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
6. Apply the migrations:
   ```
   python manage.py migrate
   ```
7. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
8. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Register a new user account.
- Login with the registered account.
- Browse the available products.
- Add products to your favorites.
- Contact the site administrators using the contact form.

## Project Structure

- `account_module`: Handles user registration, login, and password management.
- `contact_module`: Manages the contact form and user profiles.
- `eshop_project`: The main project directory containing settings and URLs.
- `home_module`: Contains views and templates for the home page and about page.
- `product_module`: Manages product listings and details.
- `site_module`: Handles site settings, footer links, and sliders.
- `static`: Contains static files such as CSS, JavaScript, and images.
- `templates`: Contains HTML templates for the project.
- `utils`: Contains utility functions such as email services.
