#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "priorityQueue.h"
#include "node.h"

using namespace std;

PriorityQueue::PriorityQueue()
{
    head = NULL;
    size = 0;
}

void PriorityQueue::enqueue(string name, char priority)
{
    Node *newNode = new Node();
    newNode->name = name;
    newNode->priority = priority;
    newNode->next = NULL;
    newNode->prev = NULL;

    if (head == NULL)
    {
        head = newNode;
    }
    else if (head->next == NULL)
    {
        if (head->priority == priority || head->priority < priority)
        {
            head->next = newNode;
            newNode->prev = head;
        }
        else
        {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
    }
    else
    {
        Node *current = head;
        bool flag = false;
        while (current->next != NULL)
        {
            if (current->priority == priority)
            {
                flag = true;
            }
            else if (current->priority != priority && flag)
            {
                break;
            }
            else if (current->priority > priority)
            {
                flag = true;
                break;
            }
            current = current->next;
        }

        if (current->next == NULL)
        {
            flag = false;
        }

        if (flag)
        {
            newNode->next = current;
            newNode->prev = current->prev;
            if (current->prev != NULL)
                current->prev->next = newNode;
            current->prev = newNode;
            if (current == head)
                head = newNode;
        }
        else if (current->next == NULL)
        {
            if (current->priority == priority || current->priority < priority)
            {
                current->next = newNode;
                newNode->prev = current;
            }
            else
            {
                newNode->next = current;
                newNode->prev = current->prev;
                if (current->prev != NULL)
                    current->prev->next = newNode;
                current->prev = newNode;
            }
        }
    }
    size++;
}

void PriorityQueue::getDotGraph(string filename)
{
    string fileNameWithExtension = filename + ".dot";
    FILE *fp = fopen(fileNameWithExtension.c_str(), "w");
    fprintf(fp, "digraph G {\n");
    fprintf(fp, "node [shape=record];\n");
    fprintf(fp, "rankdir=LR;\n");
    fprintf(fp, "node [width=1.5];\n");
    fprintf(fp, "node [height=1.5];\n");
    fprintf(fp, "node [style=filled];\n");
    fprintf(fp, "node [fillcolor=\"#EEEEEE\"];\n");
    fprintf(fp, "node [color=\"#EEEEEE\"];\n");
    fprintf(fp, "edge [color=\"#31CEF0\"];\n");

    Node *current = head;
    int i = 0;
    while (current != NULL)
    {
        fprintf(fp, "node%d [label=\"{<f0>%s|<f1>%c}\"];\n", i, current->name.c_str(), current->priority);
        current = current->next;
        i++;
    }

    current = head;
    i = 0;
    while (current != NULL)
    {
        if (current->next != NULL)
        {
            fprintf(fp, "\"node%d\":f1 -> \"node%d\":f0;\n", i, i + 1);
        }
        if (current->prev != NULL)
        {
            fprintf(fp, "\"node%d\":f0 -> \"node%d\":f1;\n", i, i - 1);
        }
        current = current->next;
        i++;
    }

    fprintf(fp, "}");
    fclose(fp);
    string command = "dot -Tpng " + filename + ".dot -o " + filename + ".png";
    system(command.c_str());
}