# Password Generator

Password Generator is a web application that allows users to generate strong passwords, save them securely, and manage their password history.

## Features

- **Password Generation:** Generate strong, random passwords with options for including numbers and special characters.

- **Password History:** View and manage your password history. Each password is timestamped for reference.

- **Password Storage:** Securely save your generated passwords for later use.

- **User Authentication:** Users can register, log in, and maintain their profile.

## Installation

To run this project locally on your computer, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/password-generator.git
   cd password-generator

## How to launch

**1.Create a Virtual Environment (Optional):**

It's a good practice to create a virtual environment to isolate your project's dependencies.

`python -m venv venv`

**2.Install Dependencies:**

Use pip to install the required dependencies from the requirements.txt file.

`pip install -r requirements.txt`

**3.Run Migrations:**

Apply the database migrations to set up the database.

`python manage.py migrate`

**4.Create a Superuser (Admin):**

To access the admin panel, create a superuser account.

`python manage.py createsuperuser`


**5.Start the Development Server:**

Start the Django development server.

`python manage.py runserver`

**6.Access the Application:**

Open your web browser and go to `http://localhost:8000` to access the Password Generator application.

# Usage

- Register for an account or log in if you already have one.
- Generate strong passwords using the Password Generator feature.
- Save generated passwords securely.
- View and manage your password history.
- Log out when you're done.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Technologies

- Django: a web framework for creating web applications.
- Python: a programming language used for application development.
- HTML, CSS, Bootstrap: for creating user interfaces.




