from website import create_app
import os

base_path = os.path.dirname(__file__)
app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
 
