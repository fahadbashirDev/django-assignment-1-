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
| URL | Description |
|---|---|
| `/` | Home page — create & view posts |
| `/signup/` | Create an account |
| `/login/` | Log in |
| `/logout/` | Log out |
| `/contact/` | Contact Us form |
| `/ml/` | ML prediction page |
| `/admin/` | Django admin panel |

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
submission.

---

## How to Submit This Assignment on Google Classroom

1. Go to **classroom.google.com** and open your class (Web Development and
   All Related).
2. Click the **Classwork** tab, find **Assignment 1**, and click it.
3. Click **View assignment** (or it may already be open).
4. Under **Your work**, you have two options — do **both** if the instructor
   asked for the GitHub link in a text/answer field as well as an attachment:
   - **Add attachment:** click **Add or create**, choose **Link**, paste your
     GitHub repository URL, and click **Add**.
   - **If there's a short-answer question box** asking for the repo link,
     type or paste the same GitHub URL there.
5. (Optional but recommended) Zip your project folder and also attach the
   `.zip` file using **Add or create → File → Upload**, in case the teacher
   wants the raw code as well as the GitHub link.
6. Double-check your **Name, Roll No., and Section** are filled in on the
   assignment cover page (print/write these on the PDF if a physical/typed
   cover sheet is required).
7. Click **Hand in** (or **Turn in**) in the top-right corner, then confirm
   by clicking **Hand in** again in the pop-up.
8. Your assignment status will change to **Handed in** / **Turned in** — that
   confirms it's submitted.

**Before submitting, make sure:**
- The GitHub repository is **public** (or shared with your instructor),
  otherwise they won't be able to open it.
- You've actually pushed all the code (`git push`) — an empty repo won't help.
- The project runs without errors (`python manage.py runserver` should work
  with no crashes).
