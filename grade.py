#!/usr/bin/python
import os
import sys
#This students dictionary maintains a mapping from UnityID -> Student's Object
students = {}
#The root path where this script file is located.
root_path = os.getcwd()
# TO EDIT: Enter the filenames which contain the `main` function Filenames are in single quotes and multiple filenames 
# are separated by commas
Main_class_files = ['']
# TO EDIT: Enter the filenames which are the Staff test cases. Multiple filenames are allowed. Enter filenames as above.
Staff_test_files = ['']
# This block processes the command line arguments.
if len(sys.argv) > 2:
	project_name = sys.argv[1]
	gradesheet = os.getcwd() + '/' + sys.argv[2]
elif len(sys.argv) > 1:
	project_name = sys.argv[1]
	gradesheet = ''
else:
	project_name = 'Default-Project'
	gradesheet = ''
#Approach for this script will be to use objects for each student and process each object separately. 
class JavaProject:
	def __init__(self,unityId):
		# The Student's Unity ID.
		self.unityId = unityId
		# List of the JAVA source files.
		self.javaSrc = [] 
		# List of the Test files provided by the student.
		self.javaTest = []
		# List of the compiled output files.
		self.javaOutput = []
		# Temp List.
		self.to_delete = []
	
	# Standard Getters, Setters and Replacers.
	def get_unityId(self):
		return self.unityId
	
	def set_javaSrc(self, javaSrc):
		if javaSrc not in self.javaSrc:
			self.javaSrc.append(javaSrc)
	
	def replace_javaSrc(self, javaSrc, newjavaSrc):
		if javaSrc in self.javaSrc:
			print 'Trying to remove --> ' + javaSrc
			position = self.javaSrc.index(javaSrc)
			self.javaSrc[position] = newjavaSrc				
			print "Modified " + str(position) + " to " + self.javaSrc[position]

	def get_javaSrc(self):
		return self.javaSrc

	def set_javaTest(self, javaTest):
		if javaTest not in self.javaTest:
			self.javaTest.append(javaTest)

	def replace_javaTest(self, javaTest, newjavaTest):
		if javaTest in self.javaTest:
			print 'Trying to remove --> ' + javaTest
			position = self.javaTest.index(javaTest)
			self.javaTest[position] = newjavaTest
			print "Modified " + str(position) + " to " + self.javaTest[position]

	def get_javaTest(self):
		return self.javaTest
	
	def get_javaOutput(self):
		return self.javaOutput

	def set_javaOutput(self, javaOutput):
		if javaOutput not in self.javaOutput:
			self.javaOutput.append(javaOutput)

	def replace_javaOutput(self, javaOutput, newjavaOutput):
		if javaOutput in self.javaOutput:
			print 'Trying to remove --> ' + javaOutput
			position = self.javaOutput.index(javaOutput)
			self.javaOutput[position] = newjavaOutput
			print "Modified " + str(position) + " to " + self.javaOutput[position]
	
	def get_list_copy(self, listA):
		listing = []
		for f in self.javaOutput:
			listing.append(f)
		return listing
	
	def remove_zero_size_files(self):
		listing = self.get_list_copy(self.javaOutput)
		for f in listing:
			print "\n\nSIZE OF file " + f + " = " + str(sizeof(f))
			if sizeof(f) == 0:	
				self.javaOutput.remove(f)
				delete_file(get_absolute_path(get_cwd(), f))
	
		listing = self.get_list_copy(self.javaSrc)	
		for f in listing:
			if sizeof(f) == 0:
				self.javaSrc.remove(f)
				delete_file(get_absolute_path(get_cwd(), f))

		listing = self.get_list_copy(self.javaTest)
		for f in listing:
			if sizeof(f) == 0:
				self.javaTest.remove(f)
				delete_file(get_absolute_path(get_cwd(), f))
	
	def get_complete_listing(self):
		file_list = ''
		for f in self.javaSrc:
			file_list += f + " "
		for f in self.javaTest:
			file_list += f + " "
		for f in self.javaOutput:
			file_list += f + " "
		return file_list
	
	def is_src_empty(self):
		if len(self.javaSrc) > 0:
			return False
		else:
			return True

	def is_test_empty(self):
		if len(self.javaTest) > 0:
			return False
		else:
			return True

# --------------------- End of Class -----------------------

# --------------------- Declare functions ------------------

def change_to_root():
	os.chdir(root_path)

def get_cwd():
	return os.getcwd()

def get_absolute_path(root, filename):
	return root + "/" + filename 

def change_dir(path):
	if os.path.exists(path):
		os.chdir(path)
		return True
	else:
		return False

def make_dir(path):
	if not (os.path.exists(path)):
		os.mkdir(path)
		return True

def delete_file(filepath):
	print "\n\nDELETING " + filepath
	if os.path.exists(filepath):
		os.system('rm ' + filepath)

def get_id_from_filename(filename):
	ID_split = filename.split('_')
	if len(ID_split) > 1:
		return ID_split[0]
	else:
		return ""

def get_type_from_filename(filename):
	Type_split = filename.split('.')
	if len(Type_split) > 1:
		return Type_split[1]
	else:
		return ''

def get_javaSrcName_from_filename(filename):
	name_split = filename.split('__')
	if len(name_split) > 1:
		return name_split[1]
	else:
		return ''

def get_classname_from_filename(filename):
	classname_split = filename.split('.')
	if len(classname_split) > 1:
		return classname_split[0]
	else:
		return ''

def src_or_test(filename):
	ftype = get_type_from_filename(filename)
	if ftype == "java":
		if filename.find('Test') != -1 or filename.find('test') != -1:
			return 'Test'
		else:
			return 'src'

def get_Testfile_path(unityId, filename, OutputType):
	return root_path + "/" + unityId + "/" +  filename + OutputType

def get_Testfile_name(filename, OutputType):
	return filename + OutputType 

def compile_errors(unityId, filename):
	if os.stat(get_Testfile_path(unityId, get_classname_from_filename(filename), 'CompileError')).st_size == 0:
		return False
	else:
		return True
	
def sizeof(filename):
	return os.stat(filename).st_size

def delete_class_files():
	os.system("rm *.class")

def delete_javaSrc_files():
	for f in Main_class_files:
		print "Deleting: "+get_cwd()+"/"+f
		if os.path.exists(get_cwd()+"/"+f):
			os.system("rm " + f)

def check_and_add_file_to_object(filename):
	unityId = get_id_from_filename(filename)
	ftype = src_or_test(filename)
	if unityId != '':
		if students.has_key(unityId) != True:
			students[unityId] = JavaProject(unityId)
	
		if ftype == 'src':
			students[unityId].set_javaSrc(filename)
		elif ftype == 'Test':
			students[unityId].set_javaTest(filename)			
		
#def process_test_folder():
	

def process_files_main_dir(home_path):
	print 'Listing: '
	print os.listdir(home_path)
	listing = os.listdir(home_path)
	for f in listing:
		check_and_add_file_to_object(f)		
	
def process_each_object():
	print "Processing Objects .. .. .. \n---------------------------------------------------------"	
	for unityId, student in students.iteritems():
		make_dir(unityId)
		print unityId + "\n---------------------"
		for f in student.get_javaSrc():
			print '-----------\n Processing Src :'+ f +'\n ----------------'
			javaSrcName = get_absolute_path(get_cwd(), get_javaSrcName_from_filename(f))
			src = get_absolute_path(get_cwd(), f)
			if javaSrcName != '':
				#cp f to javaSrcname and move to the <UnityID> folder
				os.system("cp " + src + " " + javaSrcName)
				os.system("mv " + src + " " + unityId)
			#Compile javac 
			os.system("javac " + javaSrcName + " > " + get_Testfile_path(unityId, get_classname_from_filename(f), 'CompileOutput')) 
			os.system("javac " + javaSrcName + " 2> " + get_Testfile_path(unityId, get_classname_from_filename(f), 'CompileError'))
			student.set_javaOutput(get_Testfile_name(get_classname_from_filename(f), 'CompileOutput'))
			student.set_javaOutput(get_Testfile_name(get_classname_from_filename(f), 'CompileError'))
			if get_javaSrcName_from_filename(f) in Main_class_files:
				for staff_test in Staff_test_files:
					if staff_test.find(get_classname_from_filename(get_javaSrcName_from_filename(f))) != -1:
						os.system("javac " + staff_test + " > " + get_Testfile_path(unityId, get_classname_from_filename(staff_test), 'CompileOutput'))
						os.system("javac " + staff_test + " 2> " + get_Testfile_path(unityId, get_classname_from_filename(staff_test), 'CompileError'))
						student.set_javaOutput(get_Testfile_name(get_classname_from_filename(staff_test), 'CompileOutput'))
						student.set_javaOutput(get_Testfile_name(get_classname_from_filename(staff_test), 'CompileError'))
						if compile_errors(unityId, staff_test) == False:
							os.system("java " + get_classname_from_filename(staff_test) + " > " + get_Testfile_path(unityId, get_classname_from_filename(staff_test), 'MainOutput'))
							os.system("java " + get_classname_from_filename(staff_test) + " 2> " + get_Testfile_path(unityId, get_classname_from_filename(staff_test), 'MainError'))

							student.set_javaOutput(get_Testfile_name(get_classname_from_filename(staff_test), 'MainOutput'))
							student.set_javaOutput(get_Testfile_name(get_classname_from_filename(staff_test), 'MainError'))

	
				if compile_errors(unityId, f) == False:		
					os.system("java " + get_classname_from_filename(get_javaSrcName_from_filename(f)) + " > " + get_Testfile_path(unityId, get_classname_from_filename(f), 'MainOutput'))
					os.system("java " + get_classname_from_filename(get_javaSrcName_from_filename(f)) + " 2> " + get_Testfile_path(unityId, get_classname_from_filename(f), 'MainError'))
					student.set_javaOutput(get_Testfile_name(get_classname_from_filename(f), 'MainOutput'))			
					student.set_javaOutput(get_Testfile_name(get_classname_from_filename(f), 'MainError'))		
			delete_class_files()		
	  

		for f in student.get_javaTest():
			print '---------- Tests ------------'
			javaTestName = get_absolute_path(get_cwd(), get_javaSrcName_from_filename(f))
			src = get_absolute_path(get_cwd(), f)
			if javaTestName != '':
				#cp f to javaTestName
				os.system("cp " + src + " " + javaTestName) 
				os.system("mv " + src + " " + unityId)
			#compile javac 
			os.system("javac " + javaTestName + " > " + get_Testfile_path(unityId, get_classname_from_filename(f), 'CompileOutput'))
			os.system("javac " + javaTestName + " 2> " + get_Testfile_path(unityId, get_classname_from_filename(f), 'CompileError'))
			student.set_javaOutput(get_Testfile_name(get_classname_from_filename(f), 'CompileOutput'))	
			student.set_javaOutput(get_Testfile_name(get_classname_from_filename(f), 'CompileError'))
			if compile_errors(unityId, f) == False:
				os.system("java " + get_classname_from_filename(get_javaSrcName_from_filename(f)) +" > " + get_Testfile_path(unityId, get_classname_from_filename(f), 'MainOutput'))
				os.system("java " + get_classname_from_filename(get_javaSrcName_from_filename(f)) + " 2> " + get_Testfile_path(unityId, get_classname_from_filename(f), 'MainError'))
				student.set_javaOutput(get_Testfile_name(get_classname_from_filename(f), 'MainOutput'))			
				student.set_javaOutput(get_Testfile_name(get_classname_from_filename(f), 'MainError'))		
			delete_class_files()
		print "\n"

def convert2ps(student, filename, absfilename, ftype):
	f = get_classname_from_filename(absfilename)
	if f == '':
		f = absfilename
	print '\n-----------------------------\n processing ' + filename + '\n--------------------------------------\n'
	fname = get_classname_from_filename(filename)
	if fname == '':
		fname = filename
	pdf_fname = fname + '.pdf'
	ps_fname = fname + '.ps'
			
	if ftype == 'src':
		print "removing --> " + filename
		student.replace_javaSrc(filename, pdf_fname)
	elif ftype == 'test':
		print "removing --> " + filename
		student.replace_javaTest(filename, pdf_fname)
	elif ftype == 'output':
		print "removing --> " + filename
		student.replace_javaOutput(filename, pdf_fname)

	os.system("enscript --header="+ filename + " " + absfilename + " -o " + f + ".ps")
	os.system("ps2pdf " + f + ".ps " + f + ".pdf")	
	delete_file(get_absolute_path(get_cwd(), ps_fname))
	return f + ".pdf"

def compile_pdf(unityId, file_list):
	os.system("pdftk " + gradesheet + " " + file_list + " cat output " + unityId + '-' + project_name + ".pdf" )
	os.system("rm " + file_list)


def process_pdf():
	for unityId, student in students.iteritems():
		if change_dir(unityId):
			print "\n\nChanging to : " + unityId + "\n" 
			student.remove_zero_size_files()
			listing = student.get_javaSrc()
			for f in listing:
				absfilename = get_absolute_path(get_cwd(), f)
				#print '\n\nTrying out ' + f
				if os.path.exists(f):
					print convert2ps(student, f, absfilename, 'src')
					#print f
					
			listing = student.get_javaTest()
			for f in listing:
				absfilename = get_absolute_path(get_cwd(), f)
				if os.path.exists(f):
					print convert2ps(student, f, absfilename, 'test')
			
			listing = student.get_javaOutput()
			for f in listing:
				#print "\nWE ARE ON : " + f
				absfilename = get_absolute_path(get_cwd(), f)
				f = f.strip()
				if os.path.exists(f):
					#print "ONTO --> " + absfilename
					print convert2ps(student, f, absfilename, 'output')
					delete_file(absfilename)
				else:
					print '\n\n\nERROR :' + f + ':NOT FOUND!'

			print "\n\n-------------Listing-------------\n"+student.get_complete_listing()+"\n----------------------------------------\n"
			compile_pdf(unityId, student.get_complete_listing())
		else:
			print "ERROR : No directory found for " + unityId
		change_to_root()

##Test Functions##
def print_dict(students):
	for unityId, student in students.iteritems():
		print "\n==============="
		print unityId
		print "==============="
		print "src: \n--------------" 
		print student.get_javaSrc()
		print "--------------"
		print "Test:\n--------------"
		print student.get_javaTest()
		print "--------------"
		print "Outputs:\n--------------"
		print student.get_javaOutput()

#Initiate Call to main functions.
process_files_main_dir(os.getcwd())
process_each_object()
delete_javaSrc_files()
print 'Dict : \n--------------------------------------'
print print_dict(students)
process_pdf()
print '\n\n\n ----------------------------------- Dict : \n--------------------------------------'
print print_dict(students)

