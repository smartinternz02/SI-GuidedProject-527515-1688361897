from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open(r'D:/Python/class files/Visa Prediction/Visarf.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template("Visa_index.html")

@app.route('/login', methods=["POST"])
def Guest():
    s = request.form["s"]
    if s == "ft":
        s1 = 0
    if s == "pt":
        s1 = 1
    q = request.form["ms"]
    r = request.form["as"]
    t = request.form["c"]
    if t == "cs":
        t1 = 0
    if t == "cp":
        t1 = 1
    if t == "csa":
        t1 = 2
    if t == "sd":
        t1 = 3
    if t == "rc":
        t1 = 4
    if t == "fd":
        t1 = 5
    if t == "hf":
        t1 = 6
    if t == "st":
        t1 = 7
    if t == "ce":
        t1 = 8
    if t == "bc":
        t1 = 9
    if t == "llc":
        t1 = 10
   
    outp = [[int(s1), float(q), float(r), int(t1)]]
    output = model.predict(outp)
    print(output)  
        
    return render_template("Visa_index.html",y ="The case status is " + str(output[0]))

if __name__ == '__main__':
    app.run(debug=False)

