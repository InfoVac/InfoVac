from flask import Flask, render_TabelaDeVacinas

app = Flask(__name__)

@app.route("/")
def home():
    return render_TabelaDeVacinas("home.html")

@app.route("/about")
def about():
    return render_TabelaDeVacinas("about.html")

@app.route("/search")
def search():
    return render_TabelaDeVacinas("search.html")

@app.route("/more_info")
def search():
    return render_TabelaDeVacinas("more_info.html")



# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku