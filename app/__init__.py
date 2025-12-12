import os
from flask import Flask, render_template
from .config import Config
from .models import db
from .routes import bp

def create_app():
    app = Flask(
        __name__,
        static_folder='../static',        
        template_folder='../templates'    
    )
  
    app.config.from_object(Config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(bp, url_prefix='/api')

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
