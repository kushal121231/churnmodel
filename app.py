
import numpy as np
import pandas as pd



from flask import Flask, request, render_template,jsonify

from keras.models import load_model

from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])

def home_page():

    return render_template('index.html')


@app.route("/predict", methods=["POST"])

def predict():

    


    """ Selected feature are CreditScore, Geography, Gender,

        Age, Tenure, Balance, NumOfProducts,

        HasCrCard, IsActiveMember, EstimatedSalary """

    data=[]

    CreditScore=request.form['CreditScore']

    data.append(CreditScore)

    Age=request.form['Age']

    data.append(Age)

    Tenure=request.form['Tenure']

    data.append(Tenure)

    Balance=request.form['Balance']

    data.append(Balance)

    NumOfProducts=request.form['NumOfProducts']

    data.append(NumOfProducts)

    HasCrCard=request.form['HasCrCard']

    data.append(HasCrCard)

    IsActiveMember=request.form['IsActiveMember']

    data.append(IsActiveMember)

    EstimatedSalary=request.form['EstimatedSalary']

    data.append(EstimatedSalary)


    Geography=str(request.form['Geography'])

    if(Geography=="Germany"):

        data.append(1)

        data.append(0)

    elif(Geography=='Spain'):

        data.append(0)

        data.append(1)

    else:   

        data.append(0)

        data.append(0)

    Gender=str(request.form['Gender'])

    if(Gender=='Male'):

        data.append(0)

    else:

        data.append(1)
    

    model = load_model('churn.h5')
   
    sc=StandardScaler()

    data=sc.fit_transform([data])

    single =model.predict([data])

    probability=single[0][0]




    if single[0][0] >= 0.6:

        return render_template("result.html",op1='This Customer is likely to be exited',op2=f'probability of customer leaving the bank is{probability}')

    else:

        return render_template("result.html",op1 = 'This Customer is likely to be Continue!',op2=f'probability of customer leaving the bank is {probability}')

        op1 = "This Customer is likely to be Continue!"

        #op2 = f"Confidence level is {np.round(probability[0], 2)}"


    #return render_template("index.html", op1=op1, op2=o
    




if __name__ == '__main__':

    app.run(port=80)

