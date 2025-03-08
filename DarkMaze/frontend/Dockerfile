# TODO: Install the frontend dependency package into the app folder inside the container.
FROM python:3.11

WORKDIR /app

RUN groupadd -r appgroup && \
    useradd -r -m -g appgroup -d /app appuser && \
    chmod 775 /app

COPY --chown=appuser:appgroup ./requirements.txt /app/requirements.txt
COPY --chown=appuser:appgroup ./src /app/src
RUN pip install -r /app/requirements.txt

EXPOSE 8088

USER appuser

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]
