from crypt import methods
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__,template_folder='templates')

@app.route('/')
def mainpage():
   return render_template("mainpage.html")

@app.route('/mainpage', methods =["GET", "POST"])
def load_poll():
   if request.method == "POST":
      poll_name = request.form.get("pollname")
      answer_1 = request.form.get("answer1")
      answer_2 = request.form.get("answer2")
      answer_3 = request.form.get("answer3")
      emails = request.form.get("emails")
      email_list = []
      email_list.append(emails)
      email_list = [item.split(', ') for item in email_list]
      print(email_list)
      if(poll_name != "" or answer_1 != "" or answer_2 != "" or answer_3 != "" or emails != ""):
         return render_template("pollpage.html", poll_name=poll_name, answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, emails=emails)
      else:
         warning = "Fill the details first!"
         return render_template("mainpage.html", warning=warning, emails=emails)

if __name__=='__main__':
   app.run()