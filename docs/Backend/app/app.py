from flask import Flask
from models import db
from .routes import main_routes

# Initialize Flask app
app = Flask(__name__)

# Configure app (e.g., database URI, secret key)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialize the database
db.init_app(app)

# Register routes
app.register_blueprint(main_routes)

# Main route for testing
@app.route('/')
def home():
    return "Welcome to FinHalal Website!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)
