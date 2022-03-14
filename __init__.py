from flask import Flask
from services import A,B,C
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!" 


#Endpoints
app.add_url_rule('/service-a', view_func=A.serviceA, methods=['GET', 'POST'])
app.add_url_rule('/service-b', view_func=B.serviceB, methods=['GET', 'POST'])
app.add_url_rule('/service-c', view_func=C.serviceC, methods=['GET', 'POST'])



if __name__ == '__main__':
    app.run(debug=True)
