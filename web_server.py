from flask import Flask,render_template,request,redirect
import csv
def write_to_file(data):
    # with open('database.txt',mode='a') as database:
    #     email = data['email']
    #     message = data['message']
    #     subject = data['subject']

    #     file = database.write(f'\n{email},\t{subject},\t{message}')
    with open('database.txt','a',encoding="utf-8") as database:
        i=1
        for k,v in data.items():
            file = database.write(f'{i}.{k}: {v}\n')
            i+=1
# csv-comma separated value
def write_to_csv(data):
    with open('database.csv',mode='a',newline='',encoding="utf-8") as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/<string:pg_name>")
def html_pg(pg_name):
    return render_template(pg_name)

@app.route("/submit_form", methods=['POST',"GET"])
def submit_form():
    if request.method =="POST":
        try:
            data = request.form.to_dict()
            # print(data)

            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Error, did not save to database'
    else:
        return 'something went wrong please try again' 

