from website import create_app
from flask_login import login_required, current_user


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)