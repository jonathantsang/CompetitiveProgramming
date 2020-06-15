'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    mainfunc();
});

function readline() {
    return inputString[currentLine++];
}

// First, we want to get rid of all the branches that do not contain any pho restaurants.
// After this process, all of the leaves of the tress should be pho restaurants.
// With the new tree that's formed, consider a easier problem, where we need to return back
// to our starting position.
// This is an easy solution as we just need to sum up number of roads then multiply it by 2.
// Answer = # of roads * 2.
// For this question, we do not need to return to our starting place, hence we want to subtract
// the "diameter" of the tree from the answer above.
// Answer = # of roads * 2 - diameter of the tree.
//
// Diameter of the tree is the longest distance possible from 1 vertex (restaurant) of the tree to another vertex.
//
//     6
//     |
// 1 = 2 = 3 = 4 = 5
//         |
//         7
// Diameter of the tree above is the path vertex 1 to vertex 5, denoted by "=".
// You can see that we only need to travel the road denoted by "=" once, while
// the road that is not part of the diameter "|" has to be travelled twice.


// This function will form a tree in such structure.
// tree = {
//   1: [x, y, z],
//   2: [x, y, z],
//   3: [x, y, z],
//   4: [x, y, z],
//   ...
//   N: [x, y, z]
// }
function formATree(roads, N) {
    let subTree = {};

    for (let i = 0; i < N; i++) {
        subTree[i] = new Set();
    }
    roads.forEach(road => {
        subTree[road[0]].add(road[1]);
        subTree[road[1]].add(road[0]);
    });

    return subTree;
}

// Find the subtree where all of the leaves are pho restaurants.
// If it's a leaf node, and is not a Pho restaurant, remove it.
// If it's a leaf node, and is a Pho restaurant, keep it.
// If it is not a leaf node, but contains a pho restaurant in its path, keep it.
// If it is not a leaf node, and does not contain a pho restaurant in its path, but is pho restaurant, keep it.
// If it is not a leaf node, and does not contain a pho restaurant in its path, and is not pho restaurant, remove it.
function findSubtree(tree, parent, current, M) {
    let neighbours = tree[current];
    // Current node is a leaf node.
    if (neighbours.size === 1) {

        // current node is a pho restaurant.
        if (M.has(current)) {
            return true;
        } else {
            // Current node is not a pho restaurant.
            // So we will remove this node from the tree.
            tree[parent].delete(current);
            tree[current].delete(parent);
            return false;
        }
        // The code stops here if current node is a leaf node.
    }
    // If the code skipped over the if statement above, current node is not a leaf node.


    let containsPhoRestaurant = M.has(current);
    // Check over the children of this node.
    tree[current].forEach(node => {
        // Skip the parent node.
        if (node === parent) return;
        containsPhoRestaurant = findSubtree(tree, current, node, M) || containsPhoRestaurant;
    });

    // Does not contain pho restaurants in its path.
    if (!containsPhoRestaurant) {
        tree[parent].delete(current);
        tree[current].delete(parent);
        return false;
    }

    // Does contain pho restaurants in its path.
    return true;
}
// Notice that from line 32-40 and line 56-63, the code repeats itself. Normally it is a good practice
// to combine this so we don't repeat the code, but it is left this way for clarity.

function findSubtreeBase(tree, M, current) {
    let containsPhoRestaurant = M.has(current);
    // Check over the children of this node.
    tree[current].forEach(node => {
        containsPhoRestaurant =  findSubtree(tree, current, node, M) || containsPhoRestaurant;
    });
}

function bfs(tree, start) {
    let visitedNodes = new Set();
    let queue = [];
    // queue enqueue.
    queue.push(start);
    let current = start;
    while (queue.length > 0) {
        // queue dequeue
        current = queue.shift();
        visitedNodes.add(current);
        tree[current].forEach(node => {
            if (visitedNodes.has(node)) return;
            queue.push(node);
        });
    }
    return current;
}

function dfs(tree, parent, current, prevDistance) {
    let maxDistance = prevDistance + 1;
    const tmpArray = Array.from(tree[current]);
    tmpArray.forEach(node => {
        if (node === parent) return;
        maxDistance = Math.max(maxDistance, dfs(tree, current, node, prevDistance+1))
    });

    return maxDistance;
}

function findDiameter(tree, bfsStart) {
    // Do a breadth first search (bfs) to find the furthest leaf node from ANY selected node.
    // In this case, we just selected one of the pho restaurants. (M[0])
    let start = bfs(tree, bfsStart);
    // start should be a leaf node that is furthest away from our selected node,
    // which was one of the pho restaurants. (M[0])

    let diamenterLength = 0

    // Now do a depth first search (dfs) to find the furthest node from the our starting node,
    // which was found above, and calculate the distance of it. (Number of roads in between)
    if (tree[start].size > 0) {
        diamenterLength = dfs(tree,start, tree[start].values().next().value, 0);
    }

    return diamenterLength;
}

function main(N, M, roads) {
    // Form a set for pho restaurants.
    const phoRestaurants = new Set();
    M.forEach(pho => {
        phoRestaurants.add(pho);
    });
    // Create a tree from the given input.
    let tree = formATree(roads, N);

    // Modify the tree above to only include leaves that are pho retaurants.
    findSubtreeBase(tree, phoRestaurants, M[0]);

    // Find the "diameter" of the graph (tree)
    const diameter = findDiameter(tree, M[0]);

    // Count the number of nodes (restaurants) in the tree.
    let numberOfNodes = 0;
    for (let node in tree) {
        if (tree[node].size > 0) {
            numberOfNodes++;
        }
    }

    // As described in the intro at the very top of this file,
    // do the calculation.
    const answer = (numberOfNodes - 1) * 2 - diameter;

    return answer;
}

function mainfunc(){
  var input = readline().split(" ").map(function (x) { return parseInt(x); });
  const N = input[0]; // M is [1]
  const M = readline().split(" ").map(function (x) { return parseInt(x); });

  let roads = [];
  for(var i = 0; i < N-1; i++){
    var input = readline().split(" ").map(function (x) { return parseInt(x); });
    const a = input[0];
    const b = input[1];
    roads.push([a,b]);
  }
  console.log(main(N,M,roads));
}
