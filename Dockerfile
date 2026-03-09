FROM python:3.11

# set working directory
WORKDIR /app

# copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# flask environment variables
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# expose flask port
EXPOSE 5000

# run flask
CMD ["python", "-m", "flask", "run"]

# docker build -t flask-app .
# docker run -p 5000:5000 flask-app