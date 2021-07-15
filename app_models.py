
from flask import Flask, request, render_template, redirect, url_for

from forms import TodoForm
from models import todos

###################################CZY TAK W OGÓLE MOŻNA app_models. zamiast app. ???
app_models = Flask(__name__)
app_models.config[SECRET_KEY]="ni"

@app_models.route("/todos/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            todos.create(form.data)
            todos.save_all()
        return redirect(url_for("todos_list"))

    return render_template(todos.html, form=form, todos=todos.all(), error=error)

@app_models.route("/todos/<int:todo_id>", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = todos.get(todo_id - 1)
    form = TodoForm(data=todo)

    #to be continued