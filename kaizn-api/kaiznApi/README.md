# Kaizn Backend Challenge

## About Me
<b> Name: </b> Kartiki Bhandakkar <br>
<b> Email: </b> kbhanda3@ncsu.edu

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.x)
- Django
- MySQL Server

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/kartiki-b31/Kaizn-Backend-Challenge.git
    ```

2. Navigate to the project directory:

    ```bash
    cd kaizn-api
    ```

3. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a MySQL database:

    ```sql
    CREATE DATABASE kaizn_db;
    ```

5. Configure MySQL credentials in the Django project:

    - Open `settings.py` file located in the `kaizn-api/kaiznApi` directory.
    - Find the `DATABASES` configuration section.
    - Update the `HOST`, `PORT`, `USER`, `PASSWORD`, and `NAME` values with your MySQL credentials.

6. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Access the application in your web browser at `http://localhost:8000/`.



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
