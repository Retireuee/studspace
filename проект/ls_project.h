#ifndef __LS__
#define __LS__
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <time.h>
#include <pwd.h>
#include <grp.h>

void file_info(struct stat thestat, struct dirent *thefile, struct passwd *tf, struct group *gf);

#endif
