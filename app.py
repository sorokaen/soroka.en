from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Создаем базу и таблицу
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'super_secret_flag')")
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        c.execute(query)
        result = c.fetchone()
        conn.close()

        if result:
            message = f"Welcome, {username}! The flag is: {result[2]}"
        else:
            message = "Invalid credentials!"
    
    return render_template("index.html", message=message)

if name == "__main__":
    app.run(debug=True)
