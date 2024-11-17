from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM todo')
    Title = c.fetchall()
    conn.close()
    return render_template('index.html', Title=Title)


@app.route('/add', methods=['GET'])
def add_task():
    task_content = request.args.get('text')
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('INSERT INTO todo (Title, Done) VALUES (?, ?)', (task_content, False))
    conn.commit()
    conn.close()
    return redirect('/')


@app.route('/delete/<int:Title_id>', methods=["POST"])
def delete_task(Title_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('DELETE FROM todo WHERE Title_id = ?', (Title_id,))
    conn.commit()
    conn.close()
    return redirect('/')


@app.route('/put/to/done/<string:Title>')
def put_to_done(Title):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('UPDATE todo SET Done = True WHERE Title = ?', (Title,))
    conn.commit()
    conn.close()
    return redirect('/')


@app.route('/update/task/<string:Title>', methods=["POST"])
def update(Title):
    update_task = request.form.get('task')
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('UPDATE todo SET Title = ? WHERE Title = ?', (update_task, Title))
    conn.commit()
    conn.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)



