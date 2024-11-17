from testapp import app
from flask import render_template, Flask, request


@app.route('/', methods=["GET", "POST"])
def index():
    my_dict = {
        'insert_something1' : 'views.pyのinsert_something1部分です。',
        'insert_something2': 'views.pyのinsert_something2部分です。',
    }
    return render_template('testapp/index.html', my_dict=my_dict)

@app.route('/submit', methods=['GET','POST'])
def submit():
    s_press = float(request.form['s_press'])
    d_press = float(request.form['d_press'])
    heart_rate = int(request.form['heart_rate'])
    b_temperature = float(request.form['b_temperature'])
    spo2 = int(request.form['spo2'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    
    bmi = float(weight) / (float(height) / 100) **2
    bmi_2 = ('{:.4}'.format(bmi))
    bmi_result = f'BMIは{bmi_2}です。'
    if 35.00 <= float(bmi_2) < 40.00:
        result = '測定の結果、肥満（３度）になります。'
    elif 30.00 <= float(bmi_2) < 35.00:
        result = '測定の結果、肥満（２度）になります。'
    elif 25.00 <= float(bmi_2) < 30.00:
        result = '測定の結果、肥満（１度）になります。'
    elif 18.50 <= float(bmi_2) < 25.00:
        result = '測定の結果、普通体重になります。'
    elif float(bmi_2) < 18.50:
        result = '測定の結果、痩せになります。'
    else:
        result = '測定の結果、肥満(４度)になります。'
    
    return render_template('testapp/result.html', s_press=s_press, d_press=d_press, heart_rate=heart_rate, b_temperature=b_temperature, spo2=spo2, bmi_result=bmi_result, result=result)
    
