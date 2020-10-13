from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import emp_db

app = Flask(__name__)


app.secret_key="sdsdsdsf343f3eer3"


@app.route("/")
def index():
	#get all data from db
	emp_info = emp_db.get_emplyoee_details()
	empdetails_list = []
	for e in emp_info:
		empdetails_list.append(e)
	return render_template('form.html', emplist = empdetails_list )

def setData():
	#Empty List
	empRecords = {}
	#request data from UI
	name = request.form['uname']
	mailId =  request.form['email']
	#set data to the Empty list
	empRecords["name"]=name
	empRecords["mailId"]=mailId
	return empRecords


@app.route("/", methods=['POST'])
def update_empRecords():	
	"""
	#Empty List
	empRecords = {}
	#request data from UI
	name = request.form['uname']
	designation = request.form['desg']
	contact = request.form['phone']
	address = request.form['addrs']
	mailId =  request.form['email']
	#set data to the Empty list
	empRecords["name"]=name
	empRecords["designation"]=designation
	empRecords["contact"]=contact
	empRecords["address"]=address
	empRecords["mailId"]=mailId
	"""
	empRecords = setData()
	#print records in cmd
	print(empRecords)

	emp_db.save_employee_data(empRecords)
	return redirect(url_for('index'))

#update records in DB
@app.route("/update", methods=['POST'])
def update_emp_records():	
	"""
	#Empty List
	empRecords = {}
	#request data from UI
	name = request.form['uname']
	designation = request.form['desg']
	contact = request.form['phone']
	address = request.form['addrs']
	mailId =  request.form['email']
	#set data to the Empty list
	empRecords["name"]=name
	empRecords["designation"]=designation
	empRecords["contact"]=contact
	empRecords["address"]=address
	empRecords["mailId"]=mailId
	"""
	empRecords = setData()
	#print records in cmd
	print(empRecords)
	print(request.form['id'])
	#send to db
	empid=request.form['id']
	#update_emp = emp_db.get_one_emplyoee_details(empid)
	#print(update_emp)
	emp_db.update_one_record(empid, empRecords)
	return redirect(url_for('index'))


@app.route("/delete/<emp_id>", methods=['POST'])
def deleteRecord(emp_id):
    empid = emp_id
    emp_db.delete_record(empid)
    #msg="delete "+empid+" record successfully !!!"
    return redirect(url_for('index'))



@app.route("/edit/<emp_id>", methods=['POST'])
def edit_Record(emp_id):
    empid = emp_id
    one_emp_info = emp_db.get_one_emplyoee_details(empid)
    return render_template('edit_form.html', emplist = one_emp_info)


@app.route("/remove_field/<emp_id>", methods=['POST'])
def remove_one_field(emp_id):
    empid = emp_id    
    emp_db.update_field(empid)
    return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)