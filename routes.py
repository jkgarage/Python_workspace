from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def aboutme():
  return render_template('about.html')

@app.route('/hello')
def hello():
  return 'Hellow my friend !'

if __name__ == '__main__':
  app.run(debug=True)
