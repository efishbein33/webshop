# Provet Webshop Trial Work
To properly set up the project and use it on your local please follow the following steps.

## Initial Set up
Make sure to go to directory provet_cloud

```bash
source webshop_venv/bin/activate
```

Move into project directory: 
```bash
cd webshop
```

Install project dependencies:
```bash
pip install -r requirements.txt
```

Create your .env file in your project root directory with 
your secret key and db credentials. 


run commands:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata db.json
python manage.py createsuperuser
```

The last command will walk you through the superuser account setup. After the account setup is complete, run the following to view local site:
```bash
python manage.py runserver
```

Create new products through the admin page at 127.0.0.1:8000/admin/

