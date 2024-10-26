from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) #__name__ is always unique

posts = {
    0:{
        'post_id': 0,
        'title': 'a title',
        'content': 'This is again the first one'
    }
}

@app.route('/')
def home():
    return "Hello, uwu!"

@app.route('/post/<int:post_id>') #crocodile clips, int is replaced by number of post_id. Flask unique syntax
def post(post_id): #better not to name function as variable and vice versa
    post = posts.get(post_id)
    if not post: # if post not found - None if not found; not None => True
        return render_template('404.jinja2', message=f"A post with id {post_id} was not found.")
    return render_template('post.jinja2', post=posts.get(post_id)) #we pass post argument from post.jinja2


@app.route('/post/form')
def form():
    return render_template('create.jinja2')


@app.route('/post/create', methods=['GET','POST']) #we configure so this route will only receive POST requets
def create():
    if request.method== "POST":
        title = request.form.get('title') #more secure way of reading form's payload
        content = request.form.get('content') #more secure way of reading form data
        post_id = len(posts)
        posts[post_id] = {"id":post_id, "title":title, "content":content}
        return redirect(url_for('post', post_id=post_id)) #url_for - take in function name and return url we want. def post() needs post_id and we give it in url_for
        #redirect is wrapping this "url_for" and tells the browser to load not /create/  but redirect to url_for
    return render_template('create.jinja2')

if __name__ == "__main__":
    app.run(debug=True)