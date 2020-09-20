from src.core import app

@app.route("/")
def index():
    return {"mg":"working"}

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)