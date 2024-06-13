from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(10), nullable=False)

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json
    new_expense = Expense(amount=data['amount'], category=data['category'], date=data['date'])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify(new_expense.serialize()), 201

@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([expense.serialize() for expense in expenses])

if __name__ == '__main__':
    app.run(debug=True)
