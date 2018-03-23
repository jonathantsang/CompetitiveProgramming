class Solution {
    map<string, string> totals;
    vector<string> input;
public:
    void bracketmult(int i){
        map<string, string> tempStorage;
        tempStorage.clear();
        int inputleng = input.size();
        string currE = "";
        string count = "1";
        for(int j = i; j < inputleng; j++){
            int stra;
            istringstream isss{input[j]};
            if(input[j] == ")"){
                // Peek next number              
                string mult = input[j+1];
                //cout << mult << endl;
                istringstream iss{mult};
                int mval;
                iss >> mval;
                // Update all passed by in totals
                for(map<string,string>::iterator it = tempStorage.begin(); it != tempStorage.end(); it++){
                    istringstream issp{it->second};
                    int value;
                    issp >> value;
                    value *= mval;
                    ostringstream oss;
                    oss << value;
                    it->second = oss.str();
                }
                tempStorage.clear();
            }
            else if(input[j] == "("){
                bracketmult(j);
            }
            else if (!(isss >> stra)){
                // First
                if(currE == ""){
                    tempStorage[currE] = count;
                    currE = input[j];
                    count = 1;
                    continue;
                }
                // This is an element, update old, update to new
                else if(totals.find(currE) != totals.end()){
                    totals[currE] += count;
                } else {
                    totals[currE] = count;
                }
                tempStorage[currE] = count;
                currE = input[j];
                count = 1;
            }
            // Need to update currE with count, number
            else {
                if(totals.find(currE) != totals.end()){
                    totals[currE] += count;
                    tempStorage[currE] = count;
                } else {
                    totals[currE] = count;
                    tempStorage[currE] = count;
                }
            }
        }
    }
    
    string countOfAtoms(string formula) {
        totals.clear();
        input.clear();
        int leng = formula.length();
        string currE = ""; // Current element
        string count = "1";
        bool placed = false;
        // Tokenize input
        for(int i = 0; i < leng; i++){
            // Start
            if(isupper(formula[i]) && currE == ""){
                currE = formula[i];
            } else if (isupper(formula[i]) && currE != ""){
                // Place old element in the totals
                if(totals.find(currE) != totals.end()){
                    totals[currE] += count;
                } else {
                    totals[currE] = count;
                }
                if(placed == true){
                    currE = formula[i];
                    count = "1";
                    placed = false;
                    continue;
                } else {
                    input.emplace_back(currE);
                    placed = false;
                }
                
                currE = formula[i];
                count = "1";
            } else if (islower(formula[i])){
                currE += formula[i];
            } else {
                // Else is a number then
                if(count == "1"){
                    count = formula[i];
                } else {
                    count += formula[i];
                }
                input.emplace_back(currE);
                
                string firstLetter = string(1,formula[i]);
                input.emplace_back(firstLetter);
                placed = true;
            }
        }
        // For remaining
        if(totals.find(currE) != totals.end()){
            totals[currE] += count;
        } else {
            totals[currE] = count;
        }
        
        input.emplace_back(currE);
        
        // Print input
        int inp = input.size();
        for(int i = 0; i < inp; i++){
            //cout << input[i] << endl;
        }
        
        // Go through the tokens
        for(int i = 0; i < inp; i++){
            // Normal tokens are done, just need brackets
            if(input[i] == "("){
                // Call from this one onward
                bracketmult(i);
            }
        }
        
        // Print tokens
        string final = "";
        for(map<string, string>::iterator it = totals.begin(); it != totals.end(); it++){
            //cout << it->first << " " << it->second << endl;
            istringstream isse{it->second};
            int pow;
            isse >> pow;
            if(pow == 1){
                final += it->first;
            } else {
                final += it->first + it->second;
            }            
        }
        
        //Alphabetical order
        return final;
    }
};