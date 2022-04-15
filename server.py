from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)


@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    return render_template("Read.html", users = User.get_all())

@app.route("/create")
def create():
    # call the get all classmethod to get all friends
    return render_template("Create.html", )

@app.route('/show/<user_id>', methods=["GET"])
def show(user_id):
    print(user_id)
    data = {
        'id': str(user_id),
        'check': 'check'
    }
    print(data)
    arr = User.get_one('', data = data)
    print(arr)
    name = arr[0]['first_name'] + ' ' +  arr[0]['last_name']
    email = arr[0]['email']
    up_at = arr[0]['updated_at']
    cre_at = arr[0]['created_at']
    return render_template("show.html", id12 = user_id, name = name, email = email, up_at = up_at, cre_at = cre_at)

@app.route("/edit/<id_int>/post", methods=["POST"])
def edit(id_int):
    data = {
        'id': str(id_int),
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.update(data)
    # call the get all classmethod to get all friends
    data2 = {
        'id': str(id_int)
    }
    arr = User.get_one([''], data=data2)
    print(arr)
    return render_template("edit.html", id= id_int, fname = arr['first_name'], lname = arr['last_name'], email = arr['email'])

@app.route("/edit/<id_int>", methods=["GET"])
def edit2(id_int):
    return render_template("edit.html", id= id_int)

@app.route('/delete_user/<id_user>', methods=["POST"])
def delete_user(id_user):
    data = {
        'id': str(id_user),
    }
    print('test1')
    User.delete('', data = data)
    print('test2')
    return redirect('/users')

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    print(data)
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)