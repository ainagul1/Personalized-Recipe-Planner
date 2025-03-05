# Personalized Recipe Planner

So yeah, this is a small Flask project we put together to help people organize their recipes in a way that makes sense for them. You can save your preferences, add some favorite dishes, and just keep things a bit more organized when planning meals.

## What It Does
- Saves your name and food preferences so you don’t have to enter them every time.
- Lets you add and see your personalized recipes.
- Just a simple website that does what it needs to do—nothing too fancy.

## How to Get It Running
Alright, so if you wanna try it out, here’s what you need to do:
1. First, make sure you have Python (3.7 or newer) installed.
2. You’ll also need Flask, so install it using:
   ```sh
   pip install flask
   ```
3. Once that’s done, go to the project folder:
   ```sh
   cd personalized-recipe-planner
   ```
4. Run the app:
   ```sh
   python project.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## How to Use It
- Open the homepage and enter your name + food preferences.
- Add your favorite recipes to save them.
- Check back anytime to see your saved recipes.

## What’s Inside
```
project/
│── templates/        # HTML templates for the web pages
│── static/           # CSS and JavaScript stuff
│── project.py        # The actual Flask app
│── README.md         # This file
```