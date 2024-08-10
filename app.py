import database as db
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    spells_list = db.get_spells()
    return render_template('main.html', spells = spells_list)

@app.route('/skills')
def skills():
    skills_list = db.get_skills()
    return render_template('main.html', skills = skills_list)

@app.route('/skills_peaceful')
def skills_peaceful():
    peaceful_skills_list = db.get_skills_peaceful()
    return render_template('main.html', peaceful_skills = peaceful_skills_list)

@app.route('/items')
def items():
    items_list = db.get_items()
    return render_template('main.html', items = items_list)

@app.route('/armor')
def armor():
    armor_list = db.get_armor()
    return render_template('main.html', armors = armor_list)

@app.route('/create', methods=['post', 'get'])
def create():
    message = ''
    mode = 'create'
    if request.method == "GET":
        return render_template('admin.html', form=mode)
    else:
        "Здесь будет обработка заполненной формы"

@app.route('/edit', methods=['post', 'get'])
def edit():
    message = ''
    mode = 'edit'
    if request.method == "GET":
        return render_template('admin.html', form=mode)
    else:
        "Здесь будет обработка заполненной формы"

@app.route('/delete', methods=['post', 'get'])
def delete():
    message = ''
    mode = 'delete'
    if request.method == "GET":
        return render_template('admin.html', form=mode)
    else:
        "Здесь будет обработка заполненной формы"


app.run(debug=True)
print()