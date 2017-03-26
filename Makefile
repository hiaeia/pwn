level1:
	gcc -m32 -fno-stack-protector -z execstack -o level1 level1.c
	echo 0 > /proc/sys/kernel/randomize_va_space
level2:
	gcc -m32 -fno-stack-protector -o level2 level1.c
	echo 0 > /proc/sys/kernel/randomize_va_space
level3:
	gcc -m32 -fno-stack-protector -o level3 level3.c
	echo 2 > /proc/sys/kernel/randomize_va_space
level4:
	gcc -m32 -fno-stack-protector -o level4 level3.c
	echo 2 > /proc/sys/kernel/randomize_va_space
level5:
	gcc -m32 -o level5 level3.c
	echo 2 > /proc/sys/kernel/randomize_va_space
