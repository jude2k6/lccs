from website import create_app
from flask_apscheduler import APScheduler
import subprocess,os

base_path = os.path.dirname(__file__)
app = create_app()
scheduler = APScheduler()
script_path = os.path.join(base_path, "website", "updatejson.py")

def run_update_script():
    print("job run")
    subprocess.run(["python", script_path], check=True)


scheduler.add_job(func=run_update_script, trigger="interval", minutes= 3 , id ="update", max_instances=1)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
 
