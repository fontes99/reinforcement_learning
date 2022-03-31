from copy import deepcopy
from mimetypes import init

def find_N(v, n):
    for line in range(3):
        for col in range(3):
            if (v[line][col] == n):
                return line, col

'''
{
    var inversions = 0;
    // take copy and remove blank (0) from it.
    var arr = grid.slice(0);
    arr.splice(arr.indexOf(0), 1);
    // perform sort and count swaps
    for (var i = 1; i < arr.length; i++) {
        for (var j = i - 1; j >= 0; j--) {
            if (arr[j] <= arr[j+1]) break;
            [arr[j+1], arr[j]] = [arr[j], arr[j+1]];
            inversions++;
        };
    }
    if (grid.length % 2 == 0) { // even grid width
        var size = Math.round(Math.sqrt(grid.length));
        var blankRow = Math.floor((grid.length - 1 - grid.indexOf(0)) / size);
        inversions += blankRow;
    }
    return inversions & 1; // only odd/even is needed as info
}
'''

def getParity(puzzle):
    inv_count = 0
    arr = [j for sub in puzzle for j in sub if j != 0]

    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] <= arr[j+1]: break
            arr[j+1], arr[j] = arr[j], arr[j+1];
            inv_count += 1
            
    return inv_count

goal = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

init_state = [
    [8, 1, 3],
    [0, 7, 2],
    [6, 5, 4]
]

imp = [
    [3, 4, 8],
    [1, 2, 5],
    [7, 0, 6]
]


imp2 = [
    [5, 4, 0],
    [6, 1, 8],
    [7, 3, 2]
]

i2 = [
    [8,	3, 6],
    [7,	5, 4],
    [2,	1, 0]
]

print(getParity(goal)%2 == getParity(init_state)%2)
print(getParity(goal)%2 == getParity(i2)%2)
# print([j for sub in goal for j in sub if j != 0])