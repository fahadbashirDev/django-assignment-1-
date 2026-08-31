# Django Web Application — Assignment 1

A full-stack Django web app with frontend, backend, database, authentication,
and a real Machine Learning model, built for the "Web Development and All
Related" assignment.

## Features

- **Home Page** — Facebook-style post feature. Logged-in users can create
  posts; posts are stored in the database and shown on the home page.
- **Login & Sign Up** — built with `forms.py` and Django's built-in
  authentication system. Full CRUD on posts (Create, Read, Update, Delete)
  for the logged-in user's own data.
- **Contact Us** — form that stores every submission in the database.
- **Machine Learning Page** — a RandomForest classifier trained on the Iris
  dataset (scikit-learn), deployed inside Django. Enter 4 flower measurements
  and get a real, live prediction.
- **Admin panel** — view Posts and Contact messages at `/admin/`.

## Project Structure

```
django_assignment/
├── manage.py
├── requirements.txt
├── webapp/            # project settings, urls
└── core/               # the app: models, forms, views, templates
    ├── ml/
    │   ├── train_model.py   # trains & saves the ML model
    │   └── iris_model.pkl   # the saved trained model
    └── templates/core/
```

## How to Run Locally

1. **Install dependencies** (Python 3.10+ recommended):

   ```
   pip install -r requirements.txt
   ```
2. **Train the ML model** (already included, but you can retrain it):

   ```
   python core/ml/train_model.py
   ```
3. **Run migrations:**

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **(Optional) Create an admin user:**

   ```
   python manage.py createsuperuser
   ```
5. **Start the server:**

   ```
   python manage.py runserver
   ```
6. Open your browser at **http://127.0.0.1:8000/**

## Pages

| URL           | Description                      |
| ------------- | -------------------------------- |
| `/`         | Home page — create & view posts |
| `/signup/`  | Create an account                |
| `/login/`   | Log in                           |
| `/logout/`  | Log out                          |
| `/contact/` | Contact Us form                  |
| `/ml/`      | ML prediction page               |
| `/admin/`   | Django admin panel               |

---

## How to Push This Project to GitHub

Open a terminal in the project folder and run:

```bash
git init
git add .
git commit -m "Assignment 1 - Django web app"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

> Create the empty repository first on github.com (click **New repository**,
> give it a name, don't add a README there, then copy the URL it gives you
> into the `git remote add origin ...` command above).

Copy your repository's link (it will look like
`https://github.com/your-username/your-repo-name`) — you'll need it for
submission
