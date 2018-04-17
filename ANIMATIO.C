// my first animation program..
#include<stdio.h>
#include<conio.h>
#include<graphics.h>
void main()
{
	// maximum value of x is 639 and maximum value of y is 479
	int gd=DETECT,gm,maxX,maxY,i,color;
	clrscr();
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
	maxX=getmaxx();
	maxY=getmaxy();
	for(i=0,color=14;i<=maxX;i++,color--)
	{


	setcolor(YELLOW);
	line(0,350,maxX,350);
	// The above statement is used for drawing road!

	//code to stop the bus at signal
	if(i<445)
	{
	setcolor(LIGHTBLUE);
	setfillstyle(SOLID_FILL,YELLOW);
	circle(12+i,338,12);
	circle(69+i,338,12);
	setcolor(WHITE);
	bar(0+i,296,80+i,326);
	}
	else
	{
	setcolor(LIGHTBLUE);
	circle(380,338,12);
	circle(440,338,12);
	setcolor(WHITE);
	rectangle(375,296,445,326);
	}
	// this block takes care about the car dimensions

	rectangle(500,290,560,310);
	rectangle(525,310,535,350);
	floodfill(530,310,WHITE);
	//takes care about the sign board!

	setcolor(RED);
	outtextxy(515,295,"stop");

	//plane
	if(color==0)
		color=14;
	setcolor(i);
	//tail portion after wings
	line(600-i,200,600-i,180);
	line(600-i,180,590-i,195);
	line(600-i,200,570-i,200);
	line(590-i,195,570-i,195);
	//upper wing
	line(570-i,195,570-i,175);
	line(570-i,175,560-i,195);
	//lower wing
	line(570-i,200,570-i,220);
	line(570-i,220,560-i,200);

	//part before the wings i.e. starting part
	line(560-i,195,540-i,195);
	line(560-i,200,540-i,200);
	line(540-i,195,535-i,197);
	line(540-i,200,535-i,197);


	//press any key to start:
	if(i==0)
	{
		setcolor(WHITE);
		outtextxy(50,360,"Press any key to start the animation!");
		getch();
	}


	if(i<maxX) //to keep objects visible after execution
	{
	delay(10);
	// the output will become slow by 100 miliseconds

	cleardevice();
	//clear output of previous iteration


	}
	}

	getch();
	closegraph();
}
