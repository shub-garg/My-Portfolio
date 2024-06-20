# My Portfolio

This project is a personal portfolio website built with Django, showcasing my skills, projects, and experiences. It provides a comprehensive view of my professional background and serves as a platform to highlight my work. The portfolio is hosted on Heroku for easy access.

## Features

- **Responsive Design**: The portfolio is designed to be responsive, ensuring it looks great on all devices, from desktops to mobile phones.
- **Project Showcase**: Displays detailed information about my projects, including descriptions, technologies used, and links to GitHub repositories or live demos.
- **Skills Section**: Lists my key skills and proficiencies in various technologies and tools.
- **Contact Information**: Provides a way for visitors to get in touch with me via a contact form or direct email links.
- **About Me**: Includes a brief bio and professional summary.

![portfolio-5](https://github.com/shub-garg/My-Portfolio/assets/52582943/06e185a5-0372-4f71-84bd-24690ee9d7e9)

## Technologies Used

- **Django**: Backend framework for building the website.
- **HTML/CSS**: Markup and stylesheet languages for structuring and designing the content.
- **JavaScript**: Programming language for adding interactivity and dynamic content.
- **Bootstrap**: CSS framework for responsive design.
- **Heroku**: Hosting platform for deploying the portfolio.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/shub-garg/My-Portfolio.git
cd My-Portfolio
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations and run:
```bash
python manage.py migrate
python manage.py runserver
```

5. Open your browser and navigate to:
```bash
http://localhost:8000
```

## Usage
1. Viewing Projects: Navigate through the portfolio to see detailed descriptions and links to my projects.
2. Contact Form: Use the contact form to send me a message directly from the website.
3. Skills and About Me: Learn more about my professional skills and background.

4. ## Future Enhancements
- Blog Section: Adding a blog to share insights, tutorials, and updates.
- Animations: Enhancing the visual appeal with CSS and JavaScript animations.
- Dark Mode: Implementing a dark mode toggle for better user experience.
