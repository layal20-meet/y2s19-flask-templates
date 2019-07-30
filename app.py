from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	list_tobe_passed = ["layal" ,"juna", "loai"]
	least = ["amir", "ward"]
	return render_template("index.html",list1=list_tobe_passed, opposite_day = True, least = least)

if __name__ == '__main__':
	app.run(debug = True)
