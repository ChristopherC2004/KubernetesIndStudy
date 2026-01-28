# Kubernetes Independent Study
A repository for my independent study based around learning to use Kubernetes and Docker to create a CICD workflow.

**Original goal statement:** Learn how to set up and maintain Continuous Integration/Continuous Deployment environment using Docker and Kubernetes. Learn how to use Docker and Kubernetes and their different functionalities. Build a basic editable web app to demonstrate continuous development. Given enough time left in the semester, measure performance of CI/CD solution.

#### Dependencies
##### Python
- [Plotly](https://plotly.com/python/getting-started/)
- [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
- [Flask](https://flask.palletsprojects.com/en/stable/installation/)

##### Setting up and running the app
- Run the following to set up a virtual environment 
- ```mkdir myproject | cd myproject | py -3 -m venv .venv```
- Run ```.venv\Scripts\activate``` to start up the virtual environment
- Move/Copy the templates folder and app.py file to the .venv directory
- Download flask and other dependencies into the environment 
    - ```python -m pip install flask plotly plotly[express] pandas```
- Run ```python -m flask --app app run``` to start the app