from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.datetime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

# setting up thee db at 19.50minutes
@app.route('/', method=['POST', 'GET'])

def index():
    if request .method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.sention.add(new_task)
            db.sension.commit()
        # time 27:00min
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

# @app.route('/delete/cint:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)

#     try:
#         db.sension.delete(task_to_delete)
#         db.sension.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem that task'

# @app.route('/update/<int:id>', method=['GET', 'POST'])
# def update(id):
#     task = Todo.query.get_or_404(id)

#     if request.method == 'POST':
#         task.content = request.form['content']

#         try:
#             db.sension.commit()
#             return redirect('/')
#         except:
#             return 'There is'

#     else:
#         return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)
