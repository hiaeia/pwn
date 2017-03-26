#include <stdlib.h>

void foo()
{
	char buf[128];
	read(0, buf, 255);
}
int main(int argc, char** argv)
{
	foo();
	return 0;
}
