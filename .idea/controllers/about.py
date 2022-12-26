from flask import Blueprint,render_template
about_page = Blueprint( "about_page",__name__ )

@about_page.route("/")
def about():
    return render_template( "about.html" )