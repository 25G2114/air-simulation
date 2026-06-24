#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }

    cout << endl;
    
    string a = "漢字";
    float b = 66;
    cout << a << b << endl;
}

