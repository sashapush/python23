from flask import Flask, render_template

app = Flask(__name__) #__name__ is always unique

posts = {
    0:{
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
    #f"Post is: {post['title']}, content:\n\n{post['content']}"



if __name__ == "__main__":
    app.run(debug=True)