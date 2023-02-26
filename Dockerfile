FROM python:3.8.8
WORKDIR /app


# Install dependencies
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
COPY funtions.py /app/funtions.py

RUN pip install -r requirements.txt



# Run the app
CMD ["python", "./funtions.py"]
