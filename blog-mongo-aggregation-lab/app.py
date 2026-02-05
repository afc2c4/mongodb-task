from flask import Flask, render_template, request
from services.analytics_service import (
    usuario_que_mais_comentou,
    comentario_mais_curtido
)

app = Flask(__name__)

@app.route("/")
def blog():
    return render_template("blog.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    top_user = usuario_que_mais_comentou()
    top_comment = None

    if request.method == "POST":
        post_title = request.form["post_title"]
        top_comment = comentario_mais_curtido(post_title)

    return render_template(
        "admin.html",
        top_user=top_user,
        top_comment=top_comment
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
