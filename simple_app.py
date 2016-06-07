from flask import Flask, render_template, redirect, url_for, request 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////courses.db'
db = SQLAlchemy(app)



class Courses(db.Model):
	
	crs_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(100))
	dep = db.Column(db.String(100))
	course_num = db.Column(db.Integer)
	class_time = db.Column(db.String(100))
	class_section = db.Column(db.String(100))
	class_place = db.Column(db.String(100))
	class_days = db.Column(db.String(100))
	instructor = db.Column(db.String(100))
	acad_period = db.Column(db.String(100))
	course_attrib = db.Column(db.String(100))
	CRN = db.Column(db.Integer)
	
	



	def __repr__(self):
		return "%s %d - %s  \n\t by %s \t at %s " \
		       %(self.dep,self.course_num,self.title,
		         self.instructor,self.class_place)
	
	
class Professors(db.Model):

	
	# name will be in the form "Last_Name First_initial"
	name = db.Column(db.String(100), primary_key=True)
	# Need to add first and last name
	dep = db.Column(db.String(100))
	
	def __init__(self,name,dep):
		self.name = name
		self.dep = dep

	def __repr__(self):

		return "Name:%s" (self.name)

	
def add_CSV():
	
	add_courses(get_crs_list(raw_input("CSV filename? ")))

	
def get_csv(filename):
	
	csvlist = []
	
	with open(filename) as in_file:
		for line in in_file:
			csvlist.append(line.split("\r"))
	
	csvlist = csvlist[0]
	for i in range(len(csvlist)):
		csvlist[i] = csvlist[i].split(',')
	return csvlist[1:]

def get_crs(csv_record):
	
	
	# this is dependent on the format of the csv file
	crs_place = (csv_record[8] + " " + csv_record[9]).strip()
	crs_num = int(str(csv_record[2].strip()))
	crs_acad_period = (csv_record[0].strip())
	crs_instructor = csv_record[10].strip()
	crs_crn = int(str(csv_record[4].strip()))
	return Courses(title=csv_record[5].strip(), dep =csv_record[1].strip(),
                       course_num = crs_num,class_time = csv_record[7].strip(),
                       class_place = crs_place.strip(),
                       instructor = crs_instructor.strip(),
                       acad_period = crs_acad_period,
                       class_days = csv_record[6].strip(),
                       class_section= csv_record[3].strip(),
                       course_attrib = csv_record[11].strip(),
                       CRN=crs_crn)


def get_crs_list(filename):
	csv_lst = get_csv(filename)
	
	courses = []
	for i in csv_lst:
		courses.append(get_crs(i))
		
	return courses

def add_a_course(a_course,s=db.session):

	s.add(crs)
	s.commit()	

def add_courses(crs_list,s=db.session):
	
	s.add_all(crs_list)
	s.commit()
	


def general_search(query):
	query= query.split(",")
	
	search_results= db.session.query(Courses)
	for i in query:
		searchterm =  "%" + str(i).strip() + "%"
		search_results = search_results.filter(Courses.all_data.
		                                       like(searchterm))
	
	return_val = ""
		
	for i in search_results:
		return_val += i+"<br>"		
	

	
	return_val+= str(search_results.count())+" results"


#pass a list
def filter_dep(searchterms,query_ob = db.session.query(Courses),show=False):	
	
		
	if type(searchterms) == type(""):
		searchterms= [searchterms]
		
	search_results = query_ob.filter(Courses.crs_id==0)
	
	for i in searchterms: 	
		searchterm =  "%" + i.strip() + "%"	
		search_results =search_results.union(query_ob.
		                                     filter(Courses.dep.
		                                            like(searchterm)))
	
	if show:
		for i in search_results:
			print i.all_data,"\n"		
		
		print "%d results"%(search_results.count())
	
	return search_results

#pass a list
def filter_distr(searchterms,query_ob = db.session.query(Courses),show=False):	
	
	if type(searchterms) == type(""):
		searchterms= [searchterms]	
		
	search_results = query_ob.filter(Courses.crs_id==0)
	
	for i in searchterms: 	
		searchterm =  "%" + str(i).strip() + "%"	
		search_results =search_results.\
		        union(query_ob.filter(Courses.course_attrib.
		                              like(searchterm)))
	
	if show:
		for i in search_results:
			print i.all_data,"\n"		
		
		print "%d results"%(search_results.count())		
	
	return search_results

# pass a list
def filter_time(searchterms,query_ob = db.session.query(Courses),show=False):	
	
	if type(searchterms) == type(""):
		searchterms= [searchterms]
		
	search_results = query_ob.filter(Courses.crs_id==0)
	
	for i in searchterms: 	
		searchterm =  "%" + i.strip() + "%"	
		search_results =search_results.union(query_ob.
		                                     filter(Courses.class_time.
		                                            like(searchterm)))
		
		
	if show:
		for i in search_results:
			print i.all_data,"\n"		
		
		print "%d results"%(search_results.count())	
	
	return search_results

#pass a list
def filter_prof(searchterms,query_ob = db.session.query(Courses),show=False):
	
	if type(searchterms) == type(""):
		searchterms= [searchterms]		
	
	search_results = query_ob.filter(Courses.crs_id==0)
	
	for i in searchterms: 	
		searchterm =  "%" + i.strip() + "%"	
		search_results =search_results.union(query_ob.
		                                     filter(Courses.instructor.
		                                            like(searchterm)))
	if show:
		for i in search_results:
			print i.all_data,"\n"		
		
		print "%d results"%(search_results.count())		
		
	return search_results

def filter_days(searchterm,query_ob = db.session.query(Courses),show=False):	
	
	searchterm = "  ".join(list(searchterm.replace(" ","")))
	
	searchterm =  "%" + searchterm.strip() + "%"	
	search_results = query_ob.filter(Courses.class_days.like(searchterm))
	if show:
		for i in search_results:
			print i.all_data,"\n"		
		
		print "%d results"%(search_results.count())		
	
	return search_results

#pass a list
def filter_acadPeriod(searchterms,query_ob = db.session.query(Courses),show=False):	
	
	
	if type(searchterms) == type(""):
		searchterms= [searchterms]		
	
	search_results = query_ob.filter(Courses.crs_id==0) # empty table
	
	for i in searchterms: 	
		searchterm =  "%" + i.strip() + "%"	
		search_results =search_results.union(query_ob.
		                                     filter(Courses.acad_period.
		                                            like(searchterm)))
	if show:
		for i in search_results:
			print i.all_data,"\n"		
		
		print "%d results"%(search_results.count())		
	
	return search_results

def filter_class(searchterm,query_ob = db.session.query(Courses),show=False):
	
	searchterm=searchterm.split(" ")
	q1 = filter_dep(searchterm[0],query_ob,False)
	
	searchterm =  searchterm[1].strip() + "%"
	
	search_results = q1.filter(Courses.course_num.like(searchterm))	
	if show:
		for i in search_results:
			print i.all_data,"\n"		
		
		print "%d results"%(search_results.count())		
	
	return search_results



#@app.route("/")
#def home():
	#return render_template("search_flask.html")

@app.route("/")
@app.route("/show_all")
def show_all():
	courses = Courses.query.all()
	if len(courses) > 0:
		results=[]
		for i in courses:
			record = i.instructor
			results.append(record)
		return render_template('search_flask.html', uploads=results)
	else:
		return render_template('search_flask.html')

@app.route("/filter",methods=["POST","GET"])
def process_form():
	
	if request.method == "POST":
		query_ob = db.session.query(Courses)
		
		dep = request.form["dep"].split(" or ")
		acd_prd = request.form["period"].split(" or ")
		prof = request.form["prof_form"].split(" or ")
		print request.form["prof_form"]
		day = request.form["days"]
		time = request.form["times"].split(" or ")
		for i in range(len(time)):
			time[i] = str(time[i])
			
		
		dist = request.form["distri"].split(" or ")

		
		acd_query = filter_acadPeriod(acd_prd,query_ob)
		
		dep_query = filter_dep(dep)
		
		pro_query = filter_prof(prof)
		
		day_query = filter_days(day)
		
		time_query = filter_time(time)
		
		dis_query = filter_distr(dist)	
		
		final_query = (acd_query.intersect(dep_query).
		               intersect(pro_query).intersect(day_query)
		               .intersect(time_query).intersect(dis_query))
		
	
		results=[]
		for i in final_query:
			record = [str(i.dep)+" "+str(i.course_num),i.title,i.instructor
				  ,i.class_time,i.class_days,i.course_attrib,
				  i.class_place]
			results.append(record)	
		
		return render_template("search_flask.html",search_results=results,
			                       total=str(final_query.count()))
	else:
		redirect(url_for("home"))
		

if __name__=="__main__":
	app.run()
	