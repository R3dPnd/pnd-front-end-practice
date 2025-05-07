/*
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
*/

export function longestConsecutive(nums: number[]): number {
    let numberSet = new Set<number>(nums);
    let best_streak = 0;

    numberSet.forEach(num => {
        // If the number is the start of a streak
        if (!numberSet.has(num - 1)) {
            let steak_end = num+1
            while(numberSet.has(steak_end)) {
                steak_end++;
            }
            best_streak = Math.max(best_streak, steak_end - num);
        }
    })
    return best_streak;
};