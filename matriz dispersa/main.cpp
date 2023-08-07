#include "matrix.h"

using namespace std;

int main()
{
    SparseMatrix *matrix = new SparseMatrix();
    matrix->createNode(0, 0, 1);
    matrix->createNode(0, 1, 2);
    matrix->createNode(0, 2, 3);
    matrix->createNode(1, 1, 5);
    matrix->createNode(4, 1, 7);
    matrix->createNode(1, 3, 6);
    matrix->createNode(5, 2, 1);
    matrix->createNode(1, 2, 10);
    matrix->createNode(2, 3, 100);

    matrix->getGraphviz();
    return 0;
}

// g++ -o matrix matrix.cpp main.cpp && ./matrix