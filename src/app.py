
from flask import Flask, render_template, session, request
from src.models.processdata import LookUpSC


app = Flask(__name__)
app.secret_key ="NameHere"

@app.route('/')
def homepage():
    return render_template('homepg.html')


@app.route('/profile', methods=['POST'])
def ouputvalues():
    val1 = (request.form['StCty1']).upper()
    val2 = (request.form['StCty2']).upper()
    if val1 == '':
        rt = LookUpSC.LocMissing()
        glat = rt[0]
        glong = rt[1]
        return render_template('mappic.html', glat=0, glong=0, val1='', val2='')
    else:
        rt = LookUpSC.LatLong(val1)
        glat = rt[1]
        glong = rt[2]
        return render_template('mappic.html', stcty1=val1, stcty2=val2, glat=glat, glong=glong,val1=val1, val2=val2)


if __name__ == '__main__':
    app.run(port=4996)


