from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response

app = Flask(__name__)

# Sample themes
themes = [
    {"id": 1, "name": "Theme 1"},
    {"id": 2, "name": "Theme 2"},
    {"id": 3, "name": "Theme 3"},
    {"id": 4, "name": "Template 1"},
    {"id": 5, "name": "Template 2"},
    {"id": 6, "name": "Template 3"},
    {"id": 7, "name": "New Template 1"},
    {"id": 8, "name": "New Template 2"},
    {"id": 9, "name": "New Template 3"}
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

@app.route('/preview-template/<int:theme_id>')
def preview_template(theme_id):
    theme = next((theme for theme in themes if theme["id"] == theme_id), None)
    if theme:
        return render_template('preview_template.html', theme=theme, user_data=user_data)
    return "Theme not found", 404

@app.route('/portfolio-editor', methods=['GET', 'POST'])
def portfolio_editor():
    if request.method == 'POST':
        user_data['name'] = request.form['name']
        user_data['bio'] = request.form['bio']
        projects = []
        for title, description in zip(request.form.getlist('project_titles'), request.form.getlist('project_descriptions')):
            projects.append({"title": title, "description": description})
        user_data['projects'] = projects
        return redirect(url_for('portfolio_editor'))
    return render_template('portfolio_editor.html', user_data=user_data)

@app.route('/publish', methods=['POST'])
def publish():
    return jsonify(user_data)

@app.route('/export-portfolio/<int:theme_id>', methods=['GET'])
def export_portfolio(theme_id):
    theme = next((theme for theme in themes if theme["id"] == theme_id), None)
    if theme:
        rendered_template = render_template(f'template{theme_id}.html', user_data=user_data)
        response = make_response(rendered_template)
        response.headers['Content-Disposition'] = f'attachment; filename=portfolio_{theme_id}.html'
        response.mimetype = 'text/html'
        return response
    return "Theme not found", 404

if __name__ == '__main__':
    app.run(debug=True)
