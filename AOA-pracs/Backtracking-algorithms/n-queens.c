#include <stdio.h>
#include <stdbool.h>

#define N 4

void printSolution(int board[N][N])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (board[i][j])
                printf("Q ");
            else
                printf("- ");
        }
        printf("\n");
    }
}

// Note that this function is called when "column" queens are already placed in columns from 0 to column-1. So we need to check only left side for attacking queens
bool isSafe(int board[N][N], int row, int column)
{
    int i, j;

    // Check this row on left side
    for (i = 0; i < column; i++)
        if (board[row][i])
            return false;

    // Check upper diagonal on left side
    for (i = row, j = column; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    // Check lower diagonal on left side
    for (i = row, j = column; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return false;

    return true;
}

bool solveNQueens(int board[N][N], int column)
{
    // base case
    if (column >= N)
        return true;

    for (int row = 0; row < N; row++)
    {
        if (isSafe(board, row, column))
        {
            board[row][column] = 1;

            // recursion to place rest of the queens
            if (solveNQueens(board, column + 1))
                return true;

            // BACKTRACK - if placing queen in board[i][column] doesn't lead to a solution, then remove queen from board[i][column]
            board[row][column] = 0;
        }
    }

    // if a queen can't be placed anywhere
    return false;
}

void main()
{
    int board[N][N] = {{0, 0, 0, 0},
                       {0, 0, 0, 0},
                       {0, 0, 0, 0},
                       {0, 0, 0, 0}};

    if (solveNQueens(board, 0) == false)
        printf("Solution does not exist!");
    else
        printSolution(board);
}
