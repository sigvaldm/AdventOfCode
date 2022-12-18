# Compile both programs with:
# 	$ make
#
# Program a can be used to solve part a, and takes the text file as argument:
# 	$ ./a input.txt
#
# Program ab can be used to solve either part, and takes, in addition, the number of knots as the second argument:
# 	$ ./ab input.txt 10
#
# Remove programs with
# 	$ make clean

all: a ab

%: %.cpp
	g++ -std=c++20 $< -o $@

clean:
	rm a ab
