from flask import Flask, render_template,request
import pandas as pd
from src.prediction_pipeline.model_predict import ModelPredict
import numpy as np
app=Flask(__name__)
# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')


# Define the route for prediction
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        # Get form data
        VWTI = float(request.form['VWTI'])
        SWTI = float(request.form['SWTI'])
        CWTI = float(request.form['CWTI'])
        EI = float(request.form['EI'])

        # Prepare input data for prediction
        # input_data = np.array([[VWTI, SWTI, CWTI, EI]])

        # Get the prediction
        custom_dict={"VWTI":[VWTI],"SWTI":[SWTI],"CWTI": [CWTI],"EI":[EI]}
        DF=pd.DataFrame(custom_dict)
        obj3=ModelPredict()
        result = obj3.model_prediction(DF)
        print(result)
        if result[0] == 1:
            output = "real"
        else:
            output = "fake"
        print(output)
        # Pass the result to the template
        return render_template('index.html',prediction=output)  # result[0] gives the first element in array (0 or 1)

    return render_template('index.html', prediction=None)


if __name__ == '__main__':
    app.run(debug=True)