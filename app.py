from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Sample themes
themes = [
    {"id": 1, "name": "Theme 1"},
    {"id": 2, "name": "Theme 2"},
    {"id": 3, "name": "Theme 3"}
]

# Sample user data
user_data = {
    "name": "John Doe",
    "bio": "A passionate developer.",
    "projects": [
        {"title": "Project 1", "description": "Description of project 1"},
        {"title": "Project 2", "description": "Description of project 2"}
    ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/template-chooser')
def template_chooser():
    return render_template('template_chooser.html', themes=themes)

@app.route('/portfolio-editor', methods=['GET', 'POST'])
def portfolio_editor():
    if request.method == 'POST':
        user_data['name'] = request.form['name']
        user_data['bio'] = request.form['bio']
        user_data['projects'] = request.form.getlist('projects')
        return redirect(url_for('portfolio_editor'))
    return render_template('portfolio_editor.html', user_data=user_data)

@app.route('/publish', methods=['POST'])
def publish():
    return jsonify(user_data)

if __name__ == '__main__':
    app.run(debug=True)
