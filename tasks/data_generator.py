
"""

Group 1. Collaboration with Klara, Marije, Sarab.

create a class that given a list of text files will at each iteration return
the first line of the text only if the file is not suppose to be ignored (see example files below)

example:

lets assume we have the following files and that the first line of each file is the name of the file

files = ["file1.txt", "file2.txt", "ignore_this_file1.txt", "file3.txt", "ignore_this_file1.txt", "file4.txt"]


following code should run:

>> my_generator =  DataGenerator(files)
>> for data in my_generator:
..      print(data)
..      if "3" in data:
..          break
>>"file1.txt"
>>"file2.txt"
>>"file3.txt"
>> next(my_generator)
>>"file4.txt"

"""


class DataGenerator:

	def __init__(self, data):
		self.data = data
		self.current = 0
		self.end = len(self.data)
		
	def __iter__(self):
		for filename in self.data:
			with open(filename) as f:
				first_line = f.readline()  # reads only the first line of the file
				if "ignore" not in first_line:  # only the files that should not be ignored
					self.current +=1
					yield first_line  # gives back the first line of the file
				else:
					self.current += 1
		
	def __next__(self):
		if self.current == self.end:
			raise StopIteration  # stops the iteration when there are no files left
		else:
			if "ignore" in self.data[self.current]:
				self.current += 1
				return next(self)  # if the current file should be ignored it continues to the next one
			else:
				filename = self.data[self.current]
				with open(filename) as f:
					first_line = f.readline()
					return first_line

if __name__ == '__main__':
	files = ["file1.txt", "file2.txt", "ignore_this_file1.txt", "file3.txt", "ignore_this_file2.txt", "file4.txt"]
	my_generator = DataGenerator(files)
	for data in my_generator:
		print(data)
		if "3" in data:  # tests to see if files with ignore are ignored until you reach file3
			break
	print(next(my_generator))
