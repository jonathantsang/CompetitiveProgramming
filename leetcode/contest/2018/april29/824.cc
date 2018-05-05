class Solution {
public:
    string toGoatLatin(string S) {
        string output = "";
        string str;
        string pad = "a"; // add "a" to each one
        istringstream iss{S};
        while(iss >> str){
            string newWord = "";
            // Vowel
            if(str[0] == 'a' || str[0] == 'e' || str[0] == 'i' || str[0] == 'o' || str[0] == 'u' || 
              str[0] == 'A' || str[0] == 'E' || str[0] == 'I' || str[0] == 'O' || str[0] == 'U' ){
                newWord = str;
                newWord += "ma";
                newWord += pad;
            } else {
                // Consonant
                
                // Put first character at the end
                newWord = str.substr(1);
                newWord += str[0];
                
                newWord += "ma";
                newWord += pad;
                
            }
            if(output == ""){
                output = newWord;
            } else {
                output += " " + newWord;
            }
            pad += 'a';
        }
        return output;
    }
};