#include <iostream>
#include <sstream>
class equate {
        public:
            // Appearances of x, coefficient or added
            int x;
            // What is added/subtracted by
            int factor;
            equate() : x{0}, factor{0}{}
};
std::ostream &operator<<(ostream &out, const equate eq){
    out << "x " << eq. x << " factor " << eq.factor << endl;
    return out; 
}

class Solution {
    
    vector<equate> eq;
public:
    string solveEquation(string equation) {
        eq.clear();
        // Break it down by "="
        int last = 0;
        for(int i = 0; i < equation.length(); i++){
            if(equation[i] == '=' || i+1 == equation.length()){
                if(i+1 == equation.length()){
                    i = i + 1;
                }
                // Go from last to i
                string previous = "";
                equate equ;
                bool positive = true;
                for(int j = last; j < i; j++){
                    // It can be x, +, -, or technically = but we want to avoid that
                    if(equation[j] == 'x'){
                        int n;
                        if(previous != ""){
                            istringstream iss{previous};
                            iss >> n;
                        } else {
                            n = 1;
                        }
                        if(positive)
                            equ.x += n;
                        else
                            equ.x -= n;
                        previous = "";
                    } else if (equation[j] == '+') {
                        int n;
                        if(previous != ""){
                            istringstream iss{previous};
                            iss >> n;
                        } else {
                            n = 0;
                        }
                        if(positive)
                            equ.factor += n;
                        else
                            equ.factor -= n;
                        positive = true;
                        previous = "";
                    } else if (equation[j] == '-') {
                        int n;
                        if(previous != ""){
                            istringstream iss{previous};
                            iss >> n;
                        } else {
                            n = 0;
                        }
                        if(positive)
                            equ.factor += n;
                        else
                            equ.factor -= n;
                        positive = false;
                        previous = "";
                    } else {
                        // It is a number, so add to previous
                        previous += equation[j];
                    }
                }
                // Catch last number
                if(previous != ""){
                    int n;
                    istringstream iss{previous};
                    iss >> n;
                    if(positive)
                            equ.factor += n;
                        else
                            equ.factor -= n;
                        
                }
                eq.emplace_back(equ);
                last = i + 1;
            }
        }
        // Now have different equate objects have to solve
        // Check for no solution, diff x, same factor or diff factor, same x
        for(int i = 0; i < eq.size(); i++){
            for(int j = 0; j < eq.size(); j++){
                if(i == j){
                    continue;
                }
                if((eq[i].x == eq[j].x && eq[i].factor != eq[j].factor)){
                    return "No solution";
                    break;
                } else if ((eq[i].x == eq[j].x && eq[i].factor == eq[j].factor)){
                    return "Infinite solutions";
                    break;
                }
            }
        }
        // Else have to solve old fashioned way
        // get rid of two factors
        int common = min(eq[0].factor,eq[1].factor);
        eq[0].factor -= common;
        eq[1].factor -= common;
        // Then brute force x value;
        for(int i = -1000; i < 1000; i++){
            if(eq[0].x * i + eq[0].factor == eq[1].x * i + eq[1].factor){
                ostringstream oss;
                oss << i;
                string s = oss.str();
                return "x=" + s;
            }
        }
        return "x=1";
    }
};