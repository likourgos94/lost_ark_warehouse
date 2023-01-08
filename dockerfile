FROM python
EXPOSE 5000
ADD . .
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host", "0.0.0.0"]