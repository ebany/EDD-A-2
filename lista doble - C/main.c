//create double linked list
//  Created on: 2019年10月30日

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
    int data;
    struct node *next;
    struct node *prev;
} Node;

Node *head = NULL;
Node *tail = NULL;

void insert(int data) {
    Node *newNode = (Node *) malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;

    if (head == NULL) {
        head = newNode;
        tail = newNode;
    } else {
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
    }
}

void delete(int data) {
    Node *current = head;
    while (current != NULL) {
        if (current->data == data) {
            if (current == head) {
                head = current->next;
                head->prev = NULL;
            } else if (current == tail) {
                tail = current->prev;
                tail->next = NULL;
            } else {
                current->prev->next = current->next;
                current->next->prev = current->prev;
            }
            free(current);
            return;
        }
        current = current->next;
    }
}

void print() {
    Node *current = head;
    printf("List: ");
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

void reversePrint() {
    Node *current = tail;
    printf("List: ");
    while (current != NULL) {
        printf("%d ", current->data);
        printf("%p ", current);
        current = current->prev;
    }
    printf("\n");
}

void getGraphviz() {
    FILE *fp = fopen("graphviz.txt", "w");
    fprintf(fp, "digraph G {\n");
    fprintf(fp, "rankdir=LR;\n");
    fprintf(fp, "node [shape=record];\n");
    fprintf(fp, "node [style=filled];\n");
    fprintf(fp, "node [fillcolor=\"#EEEEEE\"];\n");
    fprintf(fp, "node [color=\"#EEEEEE\"];\n");
    fprintf(fp, "edge [color=\"#31CEF0\"];\n");
    fprintf(fp, "edge [arrowhead=\"open\"];\n");
    fprintf(fp, "edge [fontname=\"Helvetica\"];\n");
    fprintf(fp, "edge [fontsize=\"10\"];\n");
    fprintf(fp, "edge [fontcolor=\"#31CEF0\"];\n");
    fprintf(fp, "edge [style=\"setlinewidth(2)\"];\n");
    Node *current = head;
    while (current != NULL) {
        fprintf(fp, "%d [label=\"<f0> |<f1> %d |<f2> \"];\n", current->data, current->data);
        current = current->next;
    }
    current = head;
    while (current != NULL) {
        if (current->next != NULL) {
            fprintf(fp, "%d:f2 -> %d:f1;\n", current->data, current->next->data);
        }
        if (current->prev != NULL) {
            fprintf(fp, "%d:f0 -> %d:f1;\n", current->data, current->prev->data);
        }
        current = current->next;
    }
    fprintf(fp, "}");
    fclose(fp);
}

int main() {
    int a = 50;
    insert(1);
    insert(2);
    insert(3);
    insert(4);
    insert(5);
    insert(6);
    insert(7);
    insert(8);
    insert(a);
    print();
    reversePrint();
    getGraphviz();
    return 0;
}