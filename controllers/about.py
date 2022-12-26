from flask import Blueprint,render_template
about_page = Blueprint( "about_page",__name__ )

@about_page.route("/<string:lan>")
def about(lan):
    return render_template( "about.html",lan=lan )