#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

int globalId = 0;

int main()
{
    vector<int> goalState;
    goalState = {1, 2, 3, 8, 0, 4, 7, 6, 5};
    cout << "Please Enter Initial Board Position ->>\n";

    vector<vector<int>> initState;
    int t;
    for (int i = 0; i < 3; i++)
    {
        vector<int> temp;
        cin >> t;
        temp.push_back(t);
        cin >> t;
        temp.push_back(t);
        cin >> t;
        temp.push_back(t);
        initState.push_back(temp);
    }

    NodeStruct *open = NULL, *close = NULL;
    double topH_val, h_val = countEucledianDist(initState);
    // cout<<"h_val: "<<h_val;
    open = insertOPEN(open, close, initState, h_val, 0);

    vector<vector<vector<int>>> nextMoves;
    int parentId;
    topH_val = h_val;

    int moveCount = 0;

    while (topH_val != 0)
    {

        nextMoves = moveGenerator(open->boardPosition);
        parentId = open->id;
        topH_val = open->hVal;
        close = insertCLOSE(close, open);
        open = removeTop(open);

        if (topH_val == 0)
        {
            break;
        }
        cout << "\nStep: " << ++moveCount;
        for (auto i = nextMoves.rbegin(); i != nextMoves.rend(); ++i)
        {
            h_val = countEucledianDist(*i);
            // cout<<h_val;
            open = insertOPEN(open, close, *i, h_val, parentId);
        }
        cout << "\nPushing Current state to close linked list.......";
        printList(close);

        cout << "\n\nPushing next stated to open linked list........";
        printList(open);
    }
    cout << "\n\n---------End:---------\n";
    cout << "\nClosed linked list.....";
    printList(close);

    cout << "\n\nOpen linked list.....";
    printList(open);

    int trialId;
    NodeStruct *temp = close;

    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    trialId = temp->id;
    cout << "\n\n*******Final Move Sequence*******\n\n";
    cout << trialId;
    printFinalMoves(close, trialId);

    return 0;
}
