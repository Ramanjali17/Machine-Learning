from WineQuality_Prediction import winequalityPrediction
from flask import Flask, request, render_template


app = Flask(__name__)
app.secret_key = "WineQuality"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Prediction", methods=['post'])
def wineDetails():
    # type,fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol
    winetype = request.form.get('type')
    fixed_acidity = float(request.form.get('fixed_acidity'))
    volatile_acidity = float(request.form.get('volatile_acidity'))
    citric_acid = float(request.form.get('citric_acid'))
    residual_sugar = float(request.form.get('residual_sugar'))
    chlorides = float(request.form.get('chlorides'))
    free_sulfur_dioxide = float(request.form.get('free_sulfur_dioxide'))
    total_sulfur_dioxide = float(request.form.get('total_sulfur_dioxide'))
    density = float(request.form.get('density'))
    ph = float(request.form.get('ph'))
    sulphates = float(request.form.get('sulphates'))
    alcohol = float(request.form.get('alcohol'))
    if winetype.lower()=="white":
        print(winetype.lower())
        typeint=1
    else:
        typeint=0
    input_data=(typeint,fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,ph,sulphates,alcohol)
    print(input_data)
    # input_data = (1,7.7,0.27,0.34,1.8,0.028,26,168,0.9911,2.99,0.48,12.1)

    if winequalityPrediction(input_data):
        submission_successful = True #or False. you can determine this.
        return render_template("index.html", submission_successful=submission_successful,message="Good Quality Wine",form="form",color="green")
        # return render_template("index.html", message="Good Quality Wine", color="green")
    else:
        submission_successful = True #or False. you can determine this.
        return render_template("index.html", submission_successful=submission_successful,message="Bad Quality Wine",form="form",color="red")
        # return render_template("index.html", message="Bad Quality Wine", color="red")       

if __name__=="__main__":
    app.run(debug=True,port=5004)
