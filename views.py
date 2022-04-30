from __init__ import *
from blogform import BlogForm


@app.route("/", methods=["POST", "GET"])
def mainpage():

    blogIter = BlogModel.query.all()

    return render_template("mainpage.html", Blog=blogIter)


@app.route("/blogCreate", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        blogform: BlogForm = BlogForm()
        UsersName: Literal[str] = request.form["UsersName"]
        blogTitle: Literal[str] = request.form["blogTitle"]
        blogBody: Literal[str] = request.form["blogBody"]
        bloginsert: Literal[str] = BlogModel(str(UsersName), str(blogTitle), str(blogBody))
        db.session.add(bloginsert)
        db.session.commit()
        return redirect("/")
    else:
        blogform: BlogForm = BlogForm()
        return render_template("blogcreate.html", form=blogform)
