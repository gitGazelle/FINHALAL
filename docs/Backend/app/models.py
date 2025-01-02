from app import db

# Define your Stock model for example
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Stock {self.name} ({self.symbol})>"

# You can add more models here as needed
