#include "node.h"
#include <stdio.h>
#include <stdlib.h>

using namespace std;

Node::Node(int value)
{
    this->value = value;
    this->next = NULL;
    this->prev = NULL;
}