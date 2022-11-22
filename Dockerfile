FROM python:3-onbuild

WORKDIR /APIwithJSON

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "flaskAPI.py"]

