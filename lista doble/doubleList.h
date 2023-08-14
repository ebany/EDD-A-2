#pragma once

#ifndef DOUBLELIST_H
#define DOUBLELIST_H

#include "node.h"
#include <string>

using namespace std;

class DoubleList
{
public:
    DoubleList();
    void add(int value);
    void remove(int value);
    void generateGraphvizFile(string fileName);

private:
    Node *head;
    void sortAsc();
    Node *search(int value);
};

#endif // !DOUBLELIST_H