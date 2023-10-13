from flask import Flask, render_template, request
import pickle
from arima2 import future_rate
from currency2 import future_rates
# from currency2 import show_graph
from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64
import statsmodels
import numpy as np

model = pickle.load(open('arima.pkl','rb'))
model = pickle.load(open('currency2.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('newtry.html')

@app.route('/predict', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        currency = request.form['currency']
        date = request.form['My_date']

        predicted = future_rate(date)
        predicted2 = future_rates(date)

        # buffer = io.BytesIO()
        # plt.savefig(buffer, format='png')
        # buffer.seek(0)
        # image_base64 = base64.b64encode(buffer.getvalue()).decode()

        # Render the HTML template with the embedded image
        # return render_template('newtry.html', image=image_base64)

        return render_template('newtry.html' , op =  predicted, op2 = predicted2)
        #     return render_template('newtry.html' ,prediction_text='Predicted rate is :{}'.format(predicted))


if __name__ == "__main__":
    app.run(debug = True)



