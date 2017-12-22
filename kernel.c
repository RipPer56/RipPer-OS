kmain()
{
	char* vidmen=(char*)0xb8000;
	vidmen[0] = 'R';
	vidmen[1] = 0x05;	
	vidmen[2] = 'i';
	vidmen[3] = 0x05;
	vidmen[4] = 'P';
	vidmen[5] = 0x05;
}
