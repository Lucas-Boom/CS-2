
from flask import Flask, render_template, request  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    #print(app.url_map)
    #print('line 17')            # Print statements go to your console
    
    return render_template("index.html")

@app.route('/save_data')
def save_data():
    fname = request.args.get("fname")

    print('name', fname)
    return render_template(
        "thanks.html"
    )

if __name__ == '__main__':  # Script executed directly?
    app.run(debug=True)  # Launch built-in web server and run this Flask webapp