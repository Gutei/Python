import sys

def hello(name):
	if name=='alice' or name=='cortona':
		name=name+'???'
	name=name+'!!!!!!'
	print('hello', name)
#main fuction
def main():
	hello (sys.argv[1])

#standart boilerplate call main
if __name__=='__main__':
	main()


