from app import app
from app import db
from posts.blueprint import posts
from flask_bootstrap import Bootstrap5
import views

Bootstrap5(app)
app.register_blueprint(posts)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ ==  "__main__":
    app.run(debug=True)