#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <regex>

using namespace std;

int main() {
    map<string, int> MNT;
    vector<string> MDT;
    map<string, vector<string>> ALA;
    vector<string> intermediate;

    cout << "Enter source program (type END to stop):" << endl;

    bool inMacro = false;
    string currentMacro;
    int mdtIndex = 0;
    string line;

    while (true) {
        getline(cin, line);
        if (line == "END" || line == "end") break;

        if (line == "MACRO" || line == "macro") {
            inMacro = true;
            getline(cin, line); // macro header
            stringstream ss(line);
            string macroName;
            ss >> macroName;
            currentMacro = macroName;
            MNT[currentMacro] = mdtIndex;

            vector<string> formals;
            string params;
            getline(ss, params);
            if (!params.empty()) {
                stringstream paramStream(params);
                string param;
                while (getline(paramStream, param, ',')) {
                    formals.push_back(param);
                }
            }
            ALA[currentMacro] = formals;
            continue;
        }

        if (inMacro) {
            if (line == "MEND" || line == "mend") {
                MDT.push_back("MEND");
                mdtIndex++;
                inMacro = false;
                currentMacro = "";
            } else {
                MDT.push_back(line);
                mdtIndex++;
            }
        } else {
            intermediate.push_back(line);
        }
    }

    // Print MNT
    cout << "\nMNT:" << endl;
    for (auto &e : MNT) {
        cout << e.first << " -> " << e.second << endl;
    }

    // Print MDT
    cout << "\nMDT:" << endl;
    for (int i = 0; i < MDT.size(); i++) {
        cout << i << " " << MDT[i] << endl;
    }

    // Print ALA
    cout << "\nALA:" << endl;
    for (auto &e : ALA) {
        cout << e.first << " -> ";
        for (auto &p : e.second) cout << p << " ";
        cout << endl;
    }

    // Print Intermediate Code
    cout << "\nIntermediate Code:" << endl;
    for (auto &s : intermediate) cout << s << endl;

    // Expand macros
    cout << "\nExpanded Code:" << endl;
    for (auto &src : intermediate) {
        stringstream ss(src);
        string first;
        ss >> first;

        if (MNT.find(first) != MNT.end()) {
            string actualPart;
            getline(ss, actualPart);
            actualPart = regex_replace(actualPart, regex("^\\s+"), ""); // trim leading spaces

            vector<string> actuals;
            if (!actualPart.empty()) {
                stringstream actualStream(actualPart);
                string a;
                while (getline(actualStream, a, ',')) actuals.push_back(a);
            }

            vector<string> formals = ALA[first];
            int idx = MNT[first];

            while (idx < MDT.size() && MDT[idx] != "MEND") {
                string body = MDT[idx];
                for (int i = 0; i < formals.size(); i++) {
                    string f = formals[i];
                    string a = i < actuals.size() ? actuals[i] : "";
                    body = regex_replace(body, regex("\\b" + f + "\\b"), a);
                }
                cout << body << endl;
                idx++;
            }
        } else {
            cout << src << endl;
        }
    }

    return 0;
}
// input 
MACRO
INCR &ARG1,&ARG2
LOAD &ARG1
ADD &ARG2
STORE &ARG1
MEND
START
INCR A,B
INCR X,Y
END
