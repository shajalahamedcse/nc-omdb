from src.core import app
from src.resource.user import user_blueprint

@app.route("/")
def index():
    return {"mg":"working"}

app.register_blueprint(user_blueprint)

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)