from blogform import BlogForm

from __init__ import *

@app.route('/', methods=['POST','GET'])
def mainpage():

    blogIter = BlogModel.query.all()
    
    return render_template('mainpage.html', Blog=blogIter)

@app.route('/blogCreate', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        blogform = BlogForm()
        UsersName = request.form['UsersName']
        blogTitle = request.form['blogTitle']
        blogBody  = request.form['blogBody']
        bloginsert = BlogModel(str(UsersName) ,str(blogTitle) ,str(blogBody))
        db.session.add(bloginsert)
        db.session.commit()
        return redirect('/')
    else:
        blogform = BlogForm()
        return render_template('blogcreate.html', form=blogform)