#include "ls_project.h"

void file_info(struct stat thestat, struct dirent *thefile, struct passwd *tf, struct group *gf) 
{
 	char buf[256]; // для представления времени в формате строки

	// 1. Тип файла		
	switch (thestat.st_mode & S_IFMT) { 
	// побитово умножая thestat.st_mode & S_IFMT мы учитываем только те биты, которые участвуют в определении типа файла (обычный файл, сокет, блочный ..)
	// после мы сравниваем полученное значение с флагами для определения типа файла 
		case S_IFBLK:  printf("b"); break; // блочное устройство
		case S_IFCHR:  printf("c"); break; // спец. файл символьного устройства 
		case S_IFDIR:  printf("d"); break; //директория 
		case S_IFIFO:  printf("p"); break; //fifo
		case S_IFLNK:  printf("l"); break; //символьная ссылка
		case S_IFSOCK: printf("s"); break; // файл типа socket
		default:       printf("-"); break; // если обычный файл
	}
	
	// 2. Права доступа
	// Здесь производится проверка на наличие соответсвующих прав для 3-х групп: владелец, группа, остальные.
	// r - чтение, w - запись, x - исполнение, "-" - нет права
	// При побитовом умножении мы получаем число в 8-ой с.с. и если оно не равно 0, то значит соотствествующее право есть
	
	// Пример: thestat.st_mode & S_IRUSR = 400. Каждая цифра отвечает за права определенной группы (владелец, группа, остальные). При переводе цифр в 2-ую с.с.
	// получаем 4 = 100 в 2-ой с.с., при этом цифры обозначают право на r, w, x. Соответственно выясняем, что у владельца есть право на чтение данного файла.
	
	// определение прав для владельца 
	printf( (thestat.st_mode & S_IRUSR) ? "r" : "-");
	printf( (thestat.st_mode & S_IWUSR) ? "w" : "-");
	printf( (thestat.st_mode & S_IXUSR) ? "x" : "-");
	
	// определение прав для группы
	printf( (thestat.st_mode & S_IRGRP) ? "r" : "-");
	printf( (thestat.st_mode & S_IWGRP) ? "w" : "-");
	printf( (thestat.st_mode & S_IXGRP) ? "x" : "-");

	// определение прав для остальных пользователей 
	printf( (thestat.st_mode & S_IROTH) ? "r" : "-");
	printf( (thestat.st_mode & S_IWOTH) ? "w" : "-");
	printf( (thestat.st_mode & S_IXOTH) ? "x" : "-");

	// 3. Количество жестких ссылок 
	printf(" %ld ", thestat.st_nlink);

	//4. владелец 
	tf = getpwuid(thestat.st_uid); // tf будет выступать структурой, хранящей инф-ию о пользователе
	printf(" %s ", tf->pw_name);

	//5. группа пользователей
	gf = getgrgid(thestat.st_gid); // gf будет выступать структурой, хранящей инф-ию о группе пользователей
	printf(" %s ", gf->gr_name);

	//6. размер файла в Кб,  время последнего изменения файла, имя файла
	strftime(buf, 256, "%d:%m %H:%M", localtime(&thestat.st_mtime)); // нужный формат представления времени
	printf(" %.2f Кб",thestat.st_size / (1024 * 1.0));
	printf(" %s", buf);
	printf(" %s\n", thefile->d_name);
}
