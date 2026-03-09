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

# Build docker image
# docker build -t flask-app .

# Run docker container
## Linux/Mac
# docker run -p 5000:5000 -v $(pwd)/data:/app/data flask-app
## Windows (PowerShell)
# docker run -p 5000:5000 -v ${PWD}/data:/app/data flask-app