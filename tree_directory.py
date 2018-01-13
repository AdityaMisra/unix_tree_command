import os
import sys

def main():
	input = sys.argv[1]

	right_aligned = False
	
	try:
		right_aligned = sys.argv[2]

		if not right_aligned == '--rtl':
			right_aligned = False
			print "Wrong input"
			return

	except IndexError:
		pass

	if right_aligned == '--rtl':
		right_aligned = True
		
	pwd = input
	path, directories, files = os.walk(input).next()
	if right_aligned:
		stdout(path+'\n')
	else:
		print path
	print_files_in_a_directory(files, right_aligned)
	print_directories_and_their_files(directories, pwd, right_aligned)

def print_files_in_a_directory(file_list, right_aligned, num_tabs=0):
	space = "	"
	for each_file in file_list:
		if right_aligned:
			if num_tabs:
				stdout("{} ---|{}|\n".format(each_file, num_tabs*4*'\t'))
			else:
				stdout("{} ---|".format(each_file))
		else:
			if num_tabs:
				print "|{}|--- {}".format(num_tabs*space, each_file)
			else:
				print "{}|--- {}".format(num_tabs*space, each_file)

def print_directories_and_their_files(directories, pwd, right_aligned, num_tabs=0):
	space = "	"
	for each_directory in directories:
		directory_name = '{}{}/'.format(pwd,each_directory)
		
		nested_path, nested_directories, nested_files = os.walk(directory_name).next()
		if right_aligned:
			if num_tabs:
				stdout("{} ---|{}|\n".format(nested_path, num_tabs*4*'\t'))
			else:	
				stdout("{} ---|".format(nested_path))

		else:
			if num_tabs:
				print "|{}|--- {}".format(num_tabs*space, nested_path)
			else:	
				print "{}|--- {}".format(num_tabs*space, nested_path)

		print_files_in_a_directory(nested_files, right_aligned, num_tabs+1)
		print_directories_and_their_files(nested_directories, directory_name, right_aligned, num_tabs+1)


def stdout(message):
    sys.stdout.write(message.rjust(134))

if __name__ == "__main__":
    main()