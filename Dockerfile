FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80
CMD ["uvicorn", "web.app:app", "--host", "0.0.0.0", "--port", "8000"]