FROM python:3.11.9-slim
COPY ./app .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "uvicorn", "main:App","--port", "8000","--host","0.0.0.0"]
