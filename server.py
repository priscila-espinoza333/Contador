from distutils.log import debug
from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    if 'count' in session: # en esta linea consulto si existe count en session
        session['count'] +=1 # si esxiste utilizamos eel codigo
    else:
        session['count'] = 0 # sino existe la pdebemos inicialir en 1


    
    return render_template('index.html')




if __name__=="__main__":
    app.run(debug=True)
