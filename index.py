from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/topten')
def TopTen():
    return render_template('topten.html')

if __name__ == '__main__':
    app.run(debug=True)