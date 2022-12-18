#include <iostream>
#include <string>
#include <fstream>
#include <array>
#include <set>
#include <cmath>
using namespace std;

using coord = array<int, 2>;

void update_head(coord &, char);
void update_tail(const coord &, coord &);

int main(int argc, char **argv){

    fstream file;
    file.open(argv[1], ios::in);

    coord head = {0,0};
    coord tail = {0,0};
    set<coord> tail_trace;
    tail_trace.insert({0,0});

    string line;
    while(getline(file, line)){
        char direction = line[0];
        int times = stoi(line.substr(2, line.length()-2));
        for(int i=0; i<times; i++){
            update_head(head, direction);
            update_tail(head, tail);
            tail_trace.insert(tail);
        }
    }

    cout << tail_trace.size() << endl;

    return 0;
}

void update_head(coord &head, char direction){
    switch(direction){
        case 'U':
            head[1] += 1;
            break;
        case 'D':
            head[1] -= 1;
            break;
        case 'L':
            head[0] -= 1;
            break;
        case 'R':
            head[0] += 1;
            break;
    }
}

void update_tail(const coord &head, coord &tail){
    coord difference;
    difference[0] = head[0] - tail[0];
    difference[1] = head[1] - tail[1];

    // Adjacent positions
    if( abs(difference[0]) <= 1 && abs(difference[1]) <= 1 ) return;

    if(difference[0]>0) tail[0]++;
    if(difference[0]<0) tail[0]--;
    if(difference[1]>0) tail[1]++;
    if(difference[1]<0) tail[1]--;
}
