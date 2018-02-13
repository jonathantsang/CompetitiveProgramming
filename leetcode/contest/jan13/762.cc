class Solution {
    
    bool checkprime(int num){
        int limit = sqrt(num) + 1;
        if(num == 1){
            return false;
        } else if (num == 2){
            return true;
        } else if (num == 3){
            return true;
        } else if (num == 5){
            return true;
        } else if (num == 7){
            return true;
        } else if (num == 11){
            return true;
        } else if (num == 13){
            return true;
        } else if (num % 2 == 0){
            return false;
        } else if (num % 3 == 0){
            return false;
        } else if (num % 5 == 0){
            return false;
        } else if (num % 7 == 0){
            return false;
        } else if (num % 11 == 0){
            return false;
        } else if (num % 13 == 0){
            return false;
        }
        int divisor = 3;
        while(divisor <= limit){
            if(num % divisor == 0){
                return false;
            }
            divisor += 2;
        }
        return true;
    }
    
    bool checkbinaryprime(int num){
        int set = 0;
        int og = num;
        while(num > 0){
            if(num % 2 == 1){
                set++;
            }
            num /= 2;
        }
        // cout << set << " num " << og << endl;
        // If set is prime
        if(checkprime(set)){
            return true;
        } else {
            return false;
        }
    }
    
public:
    int countPrimeSetBits(int L, int R) {
        int counter = 0;
        // For each number between L and R
        int num = L;
        while(num <= R){
            if(checkbinaryprime(num)){
                counter++;
            }
            num++;
        }
        return counter;
    }
};