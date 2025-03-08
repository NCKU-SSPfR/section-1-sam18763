# TODO: Install the frontend dependency package into the app folder inside the container.
FROM python:3.11

WORKDIR /app

RUN useradd -m -u 1000 user
RUN chown -R user /app
USER user

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

EXPOSE 8088

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]
