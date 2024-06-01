const lettersBase = {
    a: 0,
    b: 1,
    c: 2,
    d: 3,
    e: 4,
    f: 5,
    g: 6,
    h: 7,
    i: 8,
    j: 9,
    k: 10,
    l: 11,
    m: 12,
    n: 13,
    o: 14,
    p: 15,
    q: 16,
    r: 17,
    s: 18,
    t: 19,
    u: 20,
    v: 21,
    w: 22,
    x: 23,
    y: 24,
    z: 25
};

// automatic way to convert alphabet to number 0 - 25
function setBase() {
    let alphabetObject = {};

    for (let i = 0; i < 26; i++) {
        alphabetObject[String.fromCharCode(97 + i)] = i;
    }

    return alphabetObject
}

// matrix with vector multiplication
function matrixWithVectorMultiplication(matrix, vector) {
    let res = [];

    for (let matrixIndex = 0; matrixIndex < matrix.length; matrixIndex++) {
        let sum = 0;

        for (let vectIndex = 0; vectIndex < vector.length; vectIndex++) {
            sum += vector[vectIndex] * matrix[matrixIndex][vectIndex];
        }

        res.push(sum);
    }

    return res;
}

function hillCypher(word, key) {

    // change each of the 3 letters to a vector
    const chunks = [];
    for (let i = 0; i < word.length; i += 3) {
        chunks.push(word.slice(i, i + 3).split('').map(letter => lettersBase[letter]));
    }

    // transform each vector and then mod each letter by 26
    // and change them back to the letter 😉 
    const result = chunks.map(chunk => 
        matrixWithVectorMultiplication(key, chunk)
        .map(value => Object.keys(lettersBase)[mod(value, 26)])
        .join('')
    );

    return result.join('')
}

function encrypt(word, key) {     //! Key must be 3x3 matrix
    if (word.length === 0) return "No Word";
    if (!determinant3x3Matrices(key)) return "Key tidak memiliki determinan"

    word = word.toLowerCase();
    word = word.padEnd(Math.ceil(word.length / 3) * 3, 'x');

    return hillCypher(word, key);
}

function encryptSentance(str, key) {
    if (str.length < 1) return "Empty"
    if (!determinant3x3Matrices(key)) return "Key tidak memiliki determinan"

    let words = str.split(" ")

    let encryptedSentance = words.map(word => {
        return encrypt(word, key)
    })

    return encryptedSentance.join(" ")
}

function decrypt(word, key){  //! key is the matrix used in the encryption (before inverse)
    if (word.length === 0) return "No Word";
    if (!determinant3x3Matrices(key)) return "Key tidak memiliki determinan";

    let inversedKey = inverse(key); 
    
    return hillCypher(word, inversedKey)
}

function decryptSentance(str, key) {    //! key is the matrix used in the encryption (before inverse)
    if (str.length < 1) return "Empty"
    if (!determinant3x3Matrices(key)) return "Key tidak memiliki determinan"

    let words = str.split(" ")

    let result = words.map(word => {
        return decrypt(word, key)
    })

    return result.join(" ")
}

function determinant3x3Matrices(matrix){
    if (!Array.isArray(matrix) || matrix.length !== 3 || !matrix.every(row => Array.isArray(row) && row.length === 3)) {
        throw new Error("Input harus berupa matriks 3x3.");
    }

    const [
        [a, b, c],
        [d, e, f],
        [g, h, i]
    ] = matrix;

    const determinant = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g);

    return determinant;
}

function calculateMinor(matrix, row, col) {
    const subMatrix = matrix
        .filter((_, r) => r !== row)
        .map(r => r.filter((_, c) => c !== col));
        
    return subMatrix[0][0] * subMatrix[1][1] - subMatrix[0][1] * subMatrix[1][0];
}

function calculateCofactor(matrix, row, col) {
    const minor = calculateMinor(matrix, row, col);
    return ((row + col) % 2 === 0 ? 1 : -1) * minor;
}

function inverse(matrix) {
    if (!Array.isArray(matrix) || matrix.length !== 3 || !matrix.every(row => Array.isArray(row) && row.length === 3)) {
        throw new Error("Input harus berupa matriks 3x3.");
    }

    const determinant = determinant3x3Matrices(matrix);

    if (!determinant) {
        throw new Error("Matriks tidak memiliki invers (determinan = 0).");
    }

    const cofactors = matrix.map((row, r) => row.map((_, c) => calculateCofactor(matrix, r, c)));

    // Transpose of the cofactor matrix (adjoin)
    const adjoint = cofactors[0].map((_, c) => cofactors.map(row => row[c]));

    // Calculate inverse by dividing each element of adjoint by the determinant
    const inverse = adjoint.map(row => row.map(value => value / determinant));

    return inverse;
}

const mod = function (num, n) {
    "use strict";
    return ((num % n) + n) % n;
};

const matrix = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
];


const A = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

const B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

// console.log(inverse(matrix));
// console.log(determinant3x3Matrices(B))
// console.log("Lindan")
// console.log(encrypt("lindan", matrix))
// console.log(decrypt('oizqap', matrix))
// console.log(mod(-67, 26))
// console.log(encrypt("secretlindankerenbanget", A))
// console.log(encryptSentance("Hallo namaku lindan", A))