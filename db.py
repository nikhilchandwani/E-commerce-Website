
import os
from flask import Flask, session, render_template, request
from flask_session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
os.environ["DATABASE_URL"]='postgres://afafflhzpgqtdu:f1fafbe455a97df41e5c5cead6d0a2948c6839f0bdb5a37fa819ef7e369b9680@ec2-52-73-247-67.compute-1.amazonaws.com:5432/d4qhh809vbnvnu'
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))

db = scoped_session(sessionmaker(bind=engine))

@app.route("/",methods=['POST','GET'])
def ind():
    return render_template("index.html")
if(__name__=="__main__"):
    app.run(debug=True,use_reloader=False)