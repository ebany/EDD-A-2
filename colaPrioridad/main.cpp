#include <iostream>
#include <string>
#include "priorityQueue.h"

using namespace std;

int main()
{
    PriorityQueue *pq = new PriorityQueue();
    pq->enqueue("Proyecto 1 - A", 'A');
    pq->enqueue("Proyecto 2 - A", 'A');
    pq->enqueue("Proyecto 1 - B", 'B');
    pq->enqueue("Proyecto 2 - B", 'B');
    pq->enqueue("Proyecto 1 - C", 'C');
    pq->enqueue("Proyecto 2 - C", 'C');

    pq->getDotGraph("first");

    PriorityQueue *pq2 = new PriorityQueue();

    pq2->enqueue("Proyecto 1 - A", 'A');
    pq2->enqueue("Proyecto 2 - C", 'C');
    pq2->enqueue("Proyecto 1 - B", 'B');
    pq2->enqueue("Proyecto 2 - B", 'B');
    pq2->enqueue("Proyecto 1 - C", 'C');
    pq2->enqueue("Proyecto 2 - A", 'A');
    pq2->enqueue("Proyecto 3 - C", 'C');
    pq2->enqueue("Proyecto 3 - B", 'B');
    pq2->enqueue("Proyecto 3 - A", 'A');

    pq2->getDotGraph("second");
    return 0;
}

// commands to compile and run in one line
// g++ -o main main.cpp priorityQueue.cpp && ./main