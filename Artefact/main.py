from website import create_app
import os

#creates the app
app = create_app()

#runs the app
if __name__ == '__main__':
    app.run(debug=True)
 
