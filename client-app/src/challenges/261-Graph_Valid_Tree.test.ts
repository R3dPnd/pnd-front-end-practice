import { validTree } from "./261-Graph_Valid_Tree";

describe('validTree', () => {
    it('should return false for an empty graph', () => {
        expect(validTree(0, [])).toBe(false);
    });

    it('should return false for a graph with no edges', () => {
        expect(validTree(1, [])).toBe(false);
    });

    it('should return false for a graph with no edges', () => {
        expect(validTree(1, [[0,1],[0,2],[0,3],[1,4]])).toBe(false);
    });
});