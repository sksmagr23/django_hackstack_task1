# Moviedb Django Web App

## Description
It is a *django*-based web application used in movie data management. Users can add, edit and delete movies through Django admin interface. The site features a main page displaying list of all movies added through user admin and detail pages for every movie.

## Features
- It contains a simple navbar which contains links for home page and admin navigation.
- The entire styling of webpages is done through **Tailwind CSS** imported through cdn.
- Search functionality to filter movies by name/genre.
- It also include Pagination for better UX.
- The display contents fetches and added to pages as movie get added through admin interface through database.

## Installtion and usage
1.  **Clone the repo:**
    ```
    git clone https://github.com/sksmagr23/django_hackstack_task1.git
    cd moviedb
    ```
2. **Set up virtual environment:**
    ```
    virtualenv venv
    source venv/bin/activate
    # this setup is for linux, for windows can refer docs, also ensure that pip, python and virtualenv are installed in system
    ```
3.  **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
4.  **Apply database migrations:**
    ```
    python manage.py migrate
    ```
5.  **Create a superuser (admin):**
    ```
    python manage.py createsuperuser
    #enter the required details as per your usage
    ```  
4.  **Run the development server:**
    ```
    python manage.py runserver
    # open the url 'http://127.0.0.1:8000/'
    ```
5. **To add a movie:**
   - Navigate to admin interface using admin link in Navbar
   - Login with your superuser credentials created before
   - In the Admin interface, click on add movie and enter the movie data and click on save
   - Navigate back to home and you will see your movie added with the added format             