from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "$@&5R5mrevR5HKhy*SKAoqFYjphfE^qsj!TjpyLjjDvSirk^UxTr5eNEFFodF!MmsUG#@$QjN2x&uc6soHcLUUDeeaBZu@U%5AEEZAYfQ^ZKc^VEW5tc88i8t^3JDnVN"  # ändern!

# Passwort
PASSWORD = "Cz3$oFjyA!jL57mLPuyby^2T2^pXNNQh"

# URLs deiner Bilder
IMAGE_URLS = [
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_012_69e2.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_018_cc57.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_030_d0d5.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_035_8f6e.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_039_143c.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_046_6792.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_054_9df6.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_058_a90d.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_063_2f0b.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_071_0727.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_074_fa84.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_084_1b45.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_090_9a76.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_094_aa3b.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_098_f3fa.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_105_fd78.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_114_2b94.jpg",
    "https://cdni.hotnakedwomen.com/1280/7/655/75448606/75448606_115_254f.jpg",
    
    
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pw = request.form.get("password")
        if pw == PASSWORD:
            session["authorized"] = True
            return redirect(url_for("gallery"))
        else:
            return render_template("index.html", error="Falsches Passwort!")

    if session.get("authorized"):
        return redirect(url_for("gallery"))
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    if not session.get("authorized"):
        return redirect(url_for("index"))
    return render_template("gallery.html", images=IMAGE_URLS)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
