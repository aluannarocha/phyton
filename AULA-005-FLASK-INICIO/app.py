from flask import Flask, render_template

# criar variável que representa o server
app = Flask(__name__)

pagina = """
<h1>Fans Fans é top</h1>
<br>
<h2>Fans Fans é top</h2>
<br>
<p>Fans Fans é top<p>
"""

@app.route('/')
def index():
    return pagina

if __name__ == '__main__':
    app.run(debug=True)