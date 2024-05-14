# Django STK Push with M-Pesa Daraja API 🔥😍

This project demonstrates how to initiate an M-Pesa STK Push using the Django framework and the `django_daraja` library.

![Django Stk push](https://ibb.co/mC8CVHT)


## Prerequisites

- Python 3.8 or higher
- django_daraja library

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/django-stk-push.git
cd django-stk-push

```


### 2. Create and Activate a Virtual Environment

Create a virtual environment to manage your project dependencies. This ensures that your project uses the correct versions of packages.

```sh
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### 3. Install Dependencies

```sh
pip install -r requirments.txt
```

### 4. Configure Django Settings
Update your Django settings.py file with your M-Pesa API credentials. These credentials are necessary for authenticating your requests to the M-Pesa API.

```sh 
DARAJA_CONSUMER_KEY = 'your_consumer_key'
DARAJA_CONSUMER_SECRET = 'your_consumer_secret'
DARAJA_SHORTCODE = 'your_shortcode'
DARAJA_PASSKEY = 'your_passkey'
```
replace all of these with your actual Mpesa credentials

### 5. Run the Development Server
```sh
python manage.py runserver
```
Navigate to http://127.0.0.1:8000/ in your web browser to access your application. Enter the required details and submit the form to initiate an STK push. 😊🔥




