# limit for array size
N = 100000;

# Max size of tree
tree = [0] * (2 * N);

# function to build the tree
def build(arr) :

    # insert leaf nodes in tree
    for i in range(n) :
        tree[n + i] = arr[i];

    # build the tree by calculating parents
    for i in range(n - 1, 0, -1) :
        tree[i] = tree[i << 1] + tree[i << 1 | 1];

# function to update a tree node
def updateTreeNode(p, value) :

    # set value at position p
    tree[p + n] = value;
    p = p + n;

    # move upward and update parents
    i = p;

    while i > 1 :

        tree[i >> 1] = tree[i] + tree[i ^ 1];
        i >>= 1;

# function to get sum on interval [l, r)
def query(l, r) :

    res = 0;

    # loop to find the sum in the range
    l += n;
    r += n;

    while l < r :

        if (l & 1) :
            res += tree[l];
            l += 1

        if (r & 1) :
            r -= 1;
            res += tree[r];

        l >>= 1;
        r >>= 1

    return res;
