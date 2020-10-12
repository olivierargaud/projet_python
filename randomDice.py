# from flask import Flask
# from markupsafe import escape



# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Index Page mise a jour'

# @app.route('/hello')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/test')
# def test():
#     return 'deuxieme test!'



# @app.route('/user/<username>')	#capture un string
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)

# @app.route('/post/<int:post_id>')	#capture un int
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')	#cature un path sans l'interpreter
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % escape(subpath)



# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'






# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template("home.html", message = "Hello Vlad!")

# #if __name__ == "__main__":
# #    app.run()











# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template("home.html", message_bienvenue="Bienvenue sur la page d'accueil !")

# @app.route("/next")
# def suite():
#     return render_template("page_suivante.html")

# #if __name__ == "__main__":
# #    app.run()










from flask import Flask, request, render_template
from markupsafe import escape



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def text_box():
    text = request.form['text']
    processed_text = text.upper()
    return render_template("bienvenue.html" , message = processed_text )



@app.route('/test')
def test():
    return 'deuxieme test!'

@app.route('/contact')
def contact():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)

    

#if __name__ == '__main__':
#    app.run()