from flask import Flask, render_template, jsonify
import post_table

app = Flask(__name__)
# __name__ = main.py
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20 , 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21 , 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route('/get-items')
def get_items():
    return jsonify(post_table.get_item())


if __name__ == '__main__':
    app.run(debug=True)
