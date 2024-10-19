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
def post(post_id):
    #post = posts.get(post_id)
    return render_template('post.html', post=posts.get(post_id)) #we pass post argument from post.html
    #f"Post is: {post['title']}, content:\n\n{post['content']}"



if __name__ == "__main__":
    app.run(debug=True)