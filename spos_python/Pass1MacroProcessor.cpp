#include <iostream>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

int main() {
    map<string, int> MNT;        // Macro Name Table
    vector<string> MDT;          // Macro Definition Table
    vector<string> ALA;          // Argument List Array

    bool inMacro = false;
    string macroName;
    int mdtIndex = 0;
    string line;

    cout << "Enter program lines (type END to finish):" << endl;

    while (true) {
        getline(cin, line);
        if (line == "END") break;

        if (line == "MACRO") {
            inMacro = true;
            // Next line is macro header
            getline(cin, line);
            stringstream ss(line);
            string name, paramsPart;
            ss >> name;
            macroName = name;
            MNT[macroName] = mdtIndex;

            // Get rest of line as parameters
            getline(ss, paramsPart);
            if (!paramsPart.empty()) {
                stringstream paramStream(paramsPart);
                string param;
                while (getline(paramStream, param, ',')) {
                    // Remove leading/trailing spaces
                    param.erase(0, param.find_first_not_of(" \t"));
                    param.erase(param.find_last_not_of(" \t") + 1);
                    ALA.push_back(param);
                }
            }
            continue;
        }

        if (line == "MEND") {
            MDT.push_back("MEND");
            mdtIndex++;
            inMacro = false;
            continue;
        }

        if (inMacro) {
            MDT.push_back(line);
            mdtIndex++;
        }
    }

    // Display Tables
    cout << "\nMNT (Macro Name Table)\n----------------------" << endl;
    for (auto &entry : MNT)
        cout << entry.first << "\t" << entry.second << endl;

    cout << "\nMDT (Macro Definition Table)\n---------------------------" << endl;
    for (int i = 0; i < MDT.size(); i++)
        cout << i << "\t" << MDT[i] << endl;

    cout << "\nALA (Argument List Array)\n------------------------" << endl;
    for (int i = 0; i < ALA.size(); i++)
        cout << i << "\t" << ALA[i] << endl;

    return 0;
}
// input 
MACRO
INCR A,B
LOAD A
ADD B
STORE A
MEND
MACRO
MULT X,Y
LOAD X
MUL Y
STORE X
MEND
START
INCR 5,10
MULT 2,3
END
