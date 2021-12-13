all: exe

exe: main ls
	gcc main.o ls_project.o -o ls_project
	-rm *.o 2>/dev/null

main: main.c ls_project.h
	gcc -c main.c -o main.o

ls: ls_project.c ls_project.h
	gcc -c ls_project.c -o ls_project.o

clean:
	-rm ls_project 2>/dev/null
	
