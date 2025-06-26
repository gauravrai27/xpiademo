from flask import Flask, request, render_template_string, url_for

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
            <p><a href="/image-page">View Image Page</a></p>
        </body>
    </html>
    """
    return render_template_string(html)

@app.route('/image-page')
def image_page():
    user_text = request.args.get('q', '')
    html = """
    <html>
        <head>
            <title>Image Page</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin: 50px;
                    background-color: #f5f5f5;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    background-color: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                img {
                    max-width: 100%;
                    height: auto;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #333;
                    margin-bottom: 20px;
                }
                .nav-link {
                    color: #007bff;
                    text-decoration: none;
                    font-weight: bold;
                }
                .nav-link:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Image Gallery</h1>
                <img src="{{ url_for('static', filename='images/heck.jpg') }}" alt="Heck Image" />
                <p style="margin-top: 20px;">
                    <a href="/" class="nav-link">← Back to Home</a>
                </p>
            </div>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
