# Personal Website Portfolio

## About the App

**Personal Website Portfolio** is a full-stack web application built to showcase a professional developer's portfolio. The front end is developed using **HTML**, **CSS**, and **JavaScript**, while the back end uses **Python**, **Django**, **SQLite3**, and the **Gmail SMTP API** to handle email functionality. This application is designed to be responsive, accessible, and user-friendly across all devices.

The site features a contact form, smooth navigation using internal links, and organized content sections for clear presentation of skills and background. A scroll-to-top arrow enhances usability, and social media links are included in the footer for connectivity. The application serves as a professional, interactive résumé that enables visitors to learn more about the developer and reach out directly.

## Distinctiveness and Complexity

This portfolio web app is distinct from the CS50W course projects in that it is **not** a commerce site, wiki, social network, mail system, or search engine. Its complexity lies in its full-stack setup and the fact that it was **built entirely from scratch**, without using any boilerplate code from CS50W.

Unlike CS50W projects which follow a guided structure, this project required:
- Setting up the Django environment manually.
- Designing and implementing a complete front-end layout.
- Integrating **Gmail SMTP API** for sending emails from the contact form.
- Implementing SEO tools such as **sitemaps** and **robots.txt**.
- Structuring the application into reusable templates and modular files.

## Project Structure

The main project directory is named `CS50W Final Project` and contains the following:

### 1. `portfolio/` directory:
- `static/`
  - `script.js` – JavaScript for interactivity.
  - `styles.css` – Custom styling.
- `templates/`
  - `index.html` – Main homepage.
  - `contact.html` – Contact form page.
  - `robots.txt` – For search engine crawling control.
- `admin.py` – Registers models in Django admin.
- `apps.py` – App configuration.
- `forms.py` – Contains the contact form class.
- `models.py` – Defines data models.
- `sitemaps.py` – Generates XML sitemap.
- `urls.py` – URL patterns and page routing.
- `views.py` – Handles view logic and form processing.

### 2. `db.sqlite3` – Stores submitted contact form entries.

### 3. `manage.py` – Django’s CLI management tool.

### 4. `requirements.txt` – Lists installed packages, including Django.

## Features

- **Navigation bar** with links to main sections.
- **Scroll-to-top arrow** for easy navigation.
- **Hero section** with a welcome message.
- **About section** for personal introduction.
- **Education and Training section** listing academic background.
- **Partners section** showcasing associated companies.
- **Footer** with social media icons and “Designed by” credit.
- **Contact page** connected to **Gmail SMTP** for email submissions.
- **Logo link** in the header redirects to the homepage.

---

This project combines design, interactivity, and backend functionality to deliver a complete, dynamic portfolio experience.
