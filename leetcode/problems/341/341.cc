/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
private:
    static vector<int> values;
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for(NestedInteger &NI : nestedList){
            if(NI.isInteger()){
                NestedIterator::values.push_back(NI.getInteger());
            } else {
                NestedIterator(NI.getList());
            }
        }
    }

    int next() {
        int next = values.front();
        values.erase(values.begin());
        return next;
    }

    bool hasNext() {
        return !values.empty();
    }
};

vector<int> NestedIterator::values;

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */