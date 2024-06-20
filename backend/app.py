from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pytesseract
from PIL import Image
import io


app = Flask(__name__)

@app.route('/expenses', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']
    receipt = request.form['receipt']

    if receipt:
        img = Image.open(io.BytesIO(receipt.read()))
        text = pytesseract.image_to_string(img, lang='eng')

    expense = Expense(amount=amount, category=category, date=date)
    db.session.add(expense)
    db.session.commit()

    return jsonify({'id': expense.id}), 201

@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = []
    return jsonify(expenses)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(10), nullable=False)

db.create_all()

def categorize_expense(text):
    if 'hotel' in text.lower():
        return 'Accommodation'
    elif 'restaurant' in text.lower():
        return 'Food'

    return 'Other'


if __name__ == '__main__':
    app.run(debug=True)

