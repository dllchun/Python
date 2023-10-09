from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app6_build_weather_api/templates",
    static_folder="/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app6_build_weather_api/static",
)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station, "date": date, "temperature": temperature}


@app.route("/api/v1/translator/<word>")
def translate(word):
    if word.isupper():
        definition = word.lower()
    else:
        definition = "hello world"

    return {"word": definition, "definiton": word}


app.run(debug=True)
