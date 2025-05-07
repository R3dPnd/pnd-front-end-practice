/*
    You have a graph of n nodes labeled from 0 to n - 1. 
    You are given an integer n and a list of edges where edges[i] = [ai, bi] 
    indicates that there is an undirected edge between nodes ai and bi in the graph.

    Return true if the edges of the given graph make up a valid tree, and false otherwise.
*/

export function validTree(n: number, edges: number[][]): boolean {
    if(n === 0) return false;
    if(edges === null || edges.length === 0) return false;    
    
    const adjacencyMatrix: boolean[][] = Array.from({ length: n }, () => Array(n).fill(0));

    for(let i =0; i< edges.length; i++){
        let [a,b] = edges[i];
        adjacencyMatrix[a][b] = true;
        adjacencyMatrix[b][a] = true;
    }
    
    let visited = new Set<number>();
    let stack: number[] = [];

    while(stack.length > 0) {
        let node = stack.pop();
        if(node === undefined) break;
        if(visited.has(node)) return false;
        visited.add(node);
        for(let i = 0; i < n; i++) {
            if(adjacencyMatrix[node][i]) stack.push(i);
        }
    }
    for(let i = 0; i < n; i++) {
        if(!visited.has(i)) return false;
    }

    return true;
}
