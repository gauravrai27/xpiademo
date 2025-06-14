from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    user_text = request.args.get('q', '')
    html = f"""
    <html>
        <head><title>Text Display</title></head>
        <body>
            <h1>User Input</h1>
            <p>{user_text}</p>
            <form method="get">
                <input type="text" name="text" placeholder="Enter your text here">
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
