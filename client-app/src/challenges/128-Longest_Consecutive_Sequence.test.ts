// ... existing code ...

import { longestConsecutive } from "./128-Longest_Consecutive_Sequence";


describe('longestConsecutive', () => {
  it('returns 4 for [100,4,200,1,3,2]', () => {
    expect(longestConsecutive([100, 4, 200, 1, 3, 2])).toBe(4);
  });

  it('returns 9 for [0,3,7,2,5,8,4,6,0,1]', () => {
    expect(longestConsecutive([0,3,7,2,5,8,4,6,0,1])).toBe(9);
  });

  it('returns 3 for [1,0,1,2]', () => {
    expect(longestConsecutive([1,0,1,2])).toBe(3);
  });

  it('returns 0 for an empty array', () => {
    expect(longestConsecutive([])).toBe(0);
  });

  it('returns 1 for a single element array', () => {
    expect(longestConsecutive([42])).toBe(1);
  });

  it('returns 1 for all duplicate elements', () => {
    expect(longestConsecutive([5,5,5,5])).toBe(1);
  });

  it('handles negative numbers and mixed order', () => {
    expect(longestConsecutive([0, -1, 1, 2, -2, -3])).toBe(6);
  });

  it('returns correct result for no consecutive numbers', () => {
    expect(longestConsecutive([10, 30, 20])).toBe(1);
  });

  it('returns correct result for already sorted consecutive numbers', () => {
    expect(longestConsecutive([1,2,3,4,5])).toBe(5);
  });

  it('returns correct result for reverse sorted consecutive numbers', () => {
    expect(longestConsecutive([5,4,3,2,1])).toBe(5);
  });
});