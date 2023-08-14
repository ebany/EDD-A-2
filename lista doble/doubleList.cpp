#include <stdio.h>
#include <stdlib.h>
#include <string>
#include "node.h"
#include "doubleList.h"

using namespace std;

DoubleList::DoubleList()
{
    this->head = NULL;
}

Node *DoubleList::search(int value)
{
    Node *current = this->head;
    while (current != NULL)
    {
        if (current->value == value)
        {
            return current;
        }
        current = current->next;
    }
    return NULL;
}

void DoubleList::add(int value)
{
    Node *search = this->search(value);
    if (search != NULL)
    {
        printf("El valor %d ya existe en la lista\n", value);
        return;
    }

    Node *newNode = new Node(value);
    if (this->head == NULL)
    {
        this->head = newNode;
    }
    else
    {
        Node *current = this->head;
        while (current->next != NULL)
        {
            current = current->next;
        }
        current->next = newNode;
        newNode->prev = current;
    }
    this->sortAsc();
}

void DoubleList::sortAsc()
{
    Node *current = this->head;
    Node *index = NULL;
    int temp;

    if (this->head == NULL)
    {
        return;
    }
    else
    {
        while (current != NULL)
        {
            index = current->next;

            while (index != NULL)
            {
                if (current->value > index->value)
                {
                    temp = current->value;
                    current->value = index->value;
                    index->value = temp;
                }
                index = index->next;
            }
            current = current->next;
        }
    }
}

void DoubleList::remove(int value)
{
    Node *node = this->search(value);
    if (node == NULL)
    {
        printf("El valor %d no existe en la lista\n", value);
        return;
    }

    if (node->prev != NULL)
    {
        node->prev->next = node->next;
    }
    else
    {
        head = node->next;
    }
    if (node->next != NULL)
    {
        node->next->prev = node->prev;
    }
    delete node;
}

void DoubleList::generateGraphvizFile(string fileName)
{
    FILE *file;
    string fileNameWithExtension = fileName + ".dot";
    file = fopen(fileNameWithExtension.c_str(), "w");
    if (file != NULL)
    {
        string text = "digraph G {\n";
        text += "node [shape=record];\n";

        Node *current = this->head;
        while (current != NULL)
        {
            text += to_string(current->value) + ";\n";
            if (current->next != NULL)
            {
                text += to_string(current->value) + "->" + to_string(current->next->value) + ";\n";
            }
            if (current->prev != NULL)
            {
                text += to_string(current->value) + "->" + to_string(current->prev->value) + ";\n";
            }
            current = current->next;
        }

        text += "}";
        fputs(text.c_str(), file);
        fclose(file);

        string command = "dot -Tpng " + fileNameWithExtension + " -o " + fileName + ".png";
        system(command.c_str());
    }
    else
    {
        printf("Error al generar el archivo\n");
    }
}