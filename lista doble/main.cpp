
#include <string>
#include "doubleList.h"

using namespace std;

int main()
{
    DoubleList *list = new DoubleList();
    list->add(5);
    list->add(3);
    list->add(1);
    list->add(2);
    list->add(4);
    list->add(6);
    list->add(7);
    list->add(3);
    list->add(20);
    list->add(10);

    list->generateGraphvizFile("first");

    list->remove(3);
    list->remove(1);
    list->remove(20);

    list->generateGraphvizFile("second");

    list->add(0);
    list->add(8);
    list->add(39);

    list->generateGraphvizFile("third");

    return 0;
}

//commando to compile and run in one line
//g++ main.cpp doubleList.cpp node.cpp -o main && ./main