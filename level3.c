#include <string.h>
#include <stdlib.h>
char tips[] = "bypass aslr: leak write or read address\n";
void foo()
{
	char buf[128];
	read(0, buf, 255);
	write(1, tips, strlen(tips));
}
int main(int argc, char** argv)
{
	foo();
	return 0;
}
