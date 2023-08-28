#pragma once

#ifndef _PRIORITYQUEUE_H_
#define _PRIORITYQUEUE_H_

#include "node.h"
#include <string>

using namespace std;

class PriorityQueue
{
public:
    Node *head;
    int size;

    PriorityQueue();
    void enqueue(string name, char priority);
    void getDotGraph(string filename);
};

#endif // _PRIORITYQUEUE_H_