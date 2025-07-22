# Personal Website Portfolio

## About the App

**Personal Website Portfolio** is a full-stack web application built to showcase a professional developer's portfolio. The front end is developed using **HTML**, **CSS**, and **JavaScript**, while the back end uses **Python**, **Django**, **SQLite3**, and the **Gmail SMTP API** for email functionality. This app is designed to be responsive, accessible, and user-friendly across all devices.

The site includes a contact form, smooth navigation with internal links, and organized content sections that clearly present skills, background, and professional experience. Additionally, the site features a scroll-to-top arrow for usability and social media links in the footer for easy connectivity. The app serves as a modern, interactive résumé for the developer, allowing visitors to learn more and reach out directly.

## Distinctiveness and Complexity

This portfolio web app is distinct from other CS50W projects in several ways. Unlike typical CS50W projects (e.g., social networks, e-commerce sites, etc.), this project is focused on creating a **personal portfolio website**, which is more complex due to the following reasons:

1. **Full-Stack Setup**: 

   The app was built entirely from scratch without using any boilerplate code. Unlike other CS50W projects that follow a pre-defined structure, this project required setting up the **Django environment manually** and creating a completely custom front end.
   
2. **Custom Front-End Design**:

   A complete front-end layout was designed from scratch using HTML, CSS, and JavaScript, ensuring the site is both **responsive** and **user-friendly** across devices.

3. **Gmail SMTP Integration**: 

   The contact form uses the **Gmail SMTP API** to send emails, which required understanding and implementing email protocols securely. This was a challenging task compared to simpler form-handling projects.

4. **SEO Features**: 

   Implemented **SEO tools** such as `robots.txt` for search engine crawling control and an XML sitemap for improved search engine optimization. This added significant complexity to the project.

5. **Modular Structure**: 

   The app’s structure is highly modular, with reusable templates and separate files for different logic (e.g., `models.py`, `forms.py`). This improves scalability and maintainability, showcasing best practices for organizing Django applications.

6. **Manual Django Setup**:

   Setting up Django without relying on boilerplate code or project templates was a key part of the project. This process required deeper understanding of Django and its architecture.

These factors make this project more complex and distinct from standard CS50W projects and demonstrate my ability to work with full-stack web development.

## Project Structure

The project structure is as follows:

portfolio/
static/
script.js – JavaScript for interactivity.
styles.css – Custom styling for the site.
templates/
index.html – Main homepage.
contact.html – Contact form page.
admin.py – Registers models in Django admin.
apps.py – App configuration.
forms.py – Contains the contact form class.
models.py – Defines data models.
sitemaps.py – Generates XML sitemap.
urls.py – URL patterns and page routing.
views.py – Handles view logic and form processing.
db.sqlite3 – Stores submitted contact form entries.
manage.py – Django’s CLI management tool.
requirements.txt – Lists installed packages, including Django.

### `requirements.txt` Contents:

- `python-decouple==3.8`
- `pytz==2025.2`
- `PyYAML==6.0.2`
- `requests==2.32.4`
- `reverse==0.1.0`
- `setuptools==80.9.0`
- `sqlparse==0.5.3`
- `submit50==3.2.0`
- `termcolor==1.1.0`
- `urllib3==2.4.0`
- `wget==3.2`
- `whitenoise==6.9.0`

## Features

- **Navigation bar** with links to main sections.
- **Scroll-to-top arrow** for easy navigation.
- **Hero section** with a welcoming message.
- **About section** to introduce myself.
- **Education and Training section** listing academic background.
- **Partners section** showcasing companies I've worked with.
- **Footer** with social media links and “Designed by” credit.
- **Contact page** connected to Gmail SMTP for email submissions.
- **Logo link** in the header redirects to the homepage.

## How to Run the Application

To run this application locally, follow the steps below:

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment:
python3 -m venv venv
4. Activate the virtual environment:
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  venv\Scripts\activate
  ```
5. Install the required dependencies:
pip install -r requirements.txt
6. Apply database migrations:
python3 manage.py migrate
7. Run the development server:
python3 manage.py runserver
8. Open a web browser and navigate to `http://127.0.0.1:8000/` to view the application.

## Conclusion

This Personal Website Portfolio project allowed me to demonstrate a wide range of skills, from back-end development using Django to front-end design with HTML, CSS, and JavaScript. The project was developed from scratch and required overcoming several challenges, such as Gmail SMTP integration and implementing SEO features. The project also reflects a strong understanding of web development best practices, including building scalable, modular, and responsive applications.