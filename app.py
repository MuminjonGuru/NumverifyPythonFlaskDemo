from flask import Flask, request, redirect, url_for
import requests


app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
def index():  # put application's code here
    return 'index ../..'


@app.route('/result/<string:acc_key>/<string:number>/<string:valid>/<string:country_code>/<string:location>/<string'
           ':carrier>')
def result(acc_key, number, valid, country_code, location, carrier):
    return '<h3>Number: {};  <br> Valid: {}; <br>  Country Code: {}; <br> Location: {}; <br> Carrier: {};<br>Your ' \
           'Access Key:{} </h3>'.format(
        number, valid, country_code, location, carrier, acc_key)


@app.route('/numverify', methods=['GET', 'POST'])
def numverify():
    if request.method == 'GET':
        return '''<h1>Please fill out the parameters</h1>
                    <form method="POST" action="/numverify">
                    <input type="text" name="acc_key">
                    <input type="text" name="number">
                    <input type="submit" value="Request">
                </form>'''
    else:
        acc_key = request.form['acc_key']
        number = request.form['number']

        req = requests.get('http://apilayer.net/api/validate?access_key=' + acc_key + '&number=' + number)
        response = req.json()

        valid = response["valid"]
        country_code = response["country_code"]
        location = response["location"]
        carrier = response["carrier"]

        return redirect(url_for('result', acc_key=acc_key, number=number, valid=valid,
                                country_code=country_code, location=location, carrier=carrier))


if __name__ == '__main__':
    app.run()
