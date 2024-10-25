document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const projectsContainer = document.getElementById('projects');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const projects = [];
        projectsContainer.querySelectorAll('.project').forEach(function(project) {
            const title = project.querySelector('input[name="project_titles"]').value;
            const description = project.querySelector('textarea[name="project_descriptions"]').value;
            projects.push({ title, description });
        });
        formData.set('projects', JSON.stringify(projects));
        fetch(form.action, {
            method: form.method,
            body: formData
        }).then(response => response.json())
          .then(data => {
              console.log('Success:', data);
          })
          .catch(error => {
              console.error('Error:', error);
          });
    });
});
