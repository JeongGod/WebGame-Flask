from flask import Flask
import config


def create_app():
    # 앱 설정
    app = Flask(__name__)
    app.config.from_object(config)

    # main_view 설정
    from .views import main
    app.register_blueprint(main.bp)

    # game_view 설정
    from .views import game
    app.register_blueprint(game.bp)
    

    return app

if __name__ == "__main__":
    create_app().run()