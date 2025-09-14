FROM python:3.13-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
CMD ["python", "bot.py"]
