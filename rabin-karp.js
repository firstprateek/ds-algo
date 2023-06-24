// An implementation of text pattern matching using Rabin - Karp algorithm
// Input is a text of size m characters and a pattern of n characters
// The best case running time is O(m+n) and the worst case running time is O(m*n)
// Key idea is to have a rolling hash that has a lower chance of collision

// This implementation supports smaller length patterns
// For supporting larger patterns, modulo operator can be used to reduce the hash length

function generateHash(str) {
    let hash = 0;

    for (let i = str.length - 1; i >= 0; i--) {
        hash += str.charCodeAt(str.length - i - 1) * Math.pow(10, i);
    }
    
    return hash;
}

function findMatches(text, pattern) {
    const patternHash = generateHash(pattern);
    let curHash = generateHash(text.slice(0, pattern.length));

    let res = [];

    // Check if starting string matches
    if (curHash === patternHash && text.slice(0, pattern.length) === pattern) {
        res.push(0);
    }

    for (let i = 1; i <= text.length - pattern.length; i++) {

        curHash -= text[i - 1].charCodeAt(0) * Math.pow(10, pattern.length - 1)
        curHash *= 10
        curHash += text[i + pattern.length - 1].charCodeAt(0)

        if (curHash !== patternHash) {
            continue;
        }
        
        // Confirm if they are the same because it could be a collision
        if (text.slice(i, i + pattern.length) === pattern) {
            res.push(i);
        }
    }

    return res;
}

console.log(findMatches('abcdefgabcdefhabcde', 'abc'));
