from app.pages.controllers import pages

def register(app):
    app.register_blueprint(pages)
