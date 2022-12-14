from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    if 'count' in session: # en esta linea consulto si existe count en session
        session['count'] += 1 # si esxiste utilizamos eel codigo
    else:
        session['count'] = 0 # sino, la pdebemos inicialir en 1
    
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/incremento2')    
def incremento2():
    session['count'] +=1 
    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect('/') 

if __name__=="__main__":
    app.run(debug=True)
