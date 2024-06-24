from flask import render_template, request, redirect, url_for, current_app as app
from app import db
from app.models import Customer

@app.route('/customers')
def show_customers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@app.route('/add-customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        new_customer = Customer(first_name=first_name, last_name=last_name)
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('show_customers'))
    return render_template('add_customer.html')
