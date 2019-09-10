The errors found and how they are fixed:-
1) print stamement did have parenthesis , hence it was not a prper fuction call. By adding parenthesis the argument is passed.
2)File name was entered as mifile.txt insted of myfile.txt 
3)Program was unable to locate the file. To resolve this the entire pathname is entered as follows
     with open("\\Users\\bilwa\\code\\wtfiswronghere\\05_challenge\\myfile.txt",'r') as f: