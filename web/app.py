import os
from flask import Flask, render_template, abort

app = Flask(__name__)
app.url_map.merge_slashes = False

@app.route("/")
def hello():
    return "UOCIS docker demo!"

@app.route("/<path:name>")
def serve(name):
    if "~" in name or "//" in name or ".." in name:
        abort(403)
    if not name.endswith((".html", ".css")):
        abort(403)
    if not os.path.isfile(os.path.join(app.template_folder, name)):
        abort(404)

    return render_template(name), 200

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')