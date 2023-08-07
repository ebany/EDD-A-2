#pragma once

#ifndef _NODE_H_
#define _NODE_H_

class Node
{
public:
    int row;
    int col;
    int val;
    Node *up;
    Node *down;
    Node *left;
    Node *right;
};

#endif // _NODE_H_