from flask import Flask, render_template, request, redirect, session
import datetime
app = Flask(__name__)
app.secret_key = 'keep it secret keep it safe'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    print(request.form['strawberry'])
    print(request.form['raspberry'])
    print(request.form['apple'])
    print(request.form['first_name'])
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['items'] = (int(request.form['apple'])+int(request.form['raspberry']) + int(request.form['strawberry']) )

    return redirect("/checkout")


@app.route('/checkout')
def checkout():
    print(request.form)
    return render_template("checkout.html",
    strawberry_count=session['strawberry'],
    raspberry_count=session['raspberry'],
    apple_count=session['apple'],
    first_name=session['first_name'],
    last_name=session['last_name'],
    student_id=session['student_id'],
    items=session['items'],
    time_of_purchase=datetime.datetime.now()
    )


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
