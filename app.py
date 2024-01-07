from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    my_name = 'Piotr'
    return f"Hello, {my_name}!"

@app.route('/blog/<id>')
def blog(id):
    return f"This is blog entry #{id}"

@app.route('/message', methods=['GET', 'POST'])
def post_message():
    if request.method == 'GET':
        print("we received GET")
        return render_template("form.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect('/')
    
@app.route('/greeting')
def greeting():
    return render_template("greeting.html")

@app.route('/warehouse')
def warehouse():
    items = ['screwdriver', 'hammer', 'saw']
    return render_template('warehouse.html', items=items, errors='Błędy')