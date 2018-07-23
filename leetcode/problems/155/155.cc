class MinStack {
public:
    /** initialize your data structure here. */
    vector<int> values;
    vector<int> min;
    MinStack() {
        // ok
    }
    
    void push(int x) {
        values.push_back(x);
        int minNow = 0;
        if(min.size() == 0){
            minNow = x;   
        } else {
            minNow = min.back() > x ? x : min.back();
        }
        min.push_back(minNow);
    }
    
    void pop() {
        values.pop_back();
        min.pop_back();
    }
    
    int top() {
        return values.back();
    }
    
    int getMin() {
        return min.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */