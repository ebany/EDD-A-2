#pragma once

#ifndef _NODE_H_
#define _NODE_H_

#include <string>

using namespace std;

class Node
{
public:
    string name;
    char priority;
    Node *next;
    Node *prev;
};

#endif // _NODE_H_