from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return ("Hello world!")

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<int:num>')
def play_times(num):
    return render_template("play2.html", num=num)

@app.route('/play/<int:num>/<string:color>')
def play_times_color(num,color):
    return render_template("play3.html", num=num, color = color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.