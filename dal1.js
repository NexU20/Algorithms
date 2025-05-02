// nodejs_min_max_compare_comparisons.js

const { performance } = require("perf_hooks");

// Brute Force: hitung jumlah komparasi secara eksplisit
function bruteForce(arr) {
  let min = arr[0],
    max = arr[0];
  let comparisons = 0;

  for (let i = 1; i < arr.length; i++) {
    comparisons++;
    if (arr[i] < min) {
      min = arr[i];
    }
    comparisons++;
    if (arr[i] > max) {
      max = arr[i];
    }
  }

  return { min, max, comparisons };
}

// Divide and Conquer: hitung komparasi dalam objek counter
function divideAndConquer(arr, low, high, counter) {
  if (low === high) {
    return { min: arr[low], max: arr[low] };
  }

  if (high === low + 1) {
    counter.count++;
    if (arr[low] < arr[high]) {
      return { min: arr[low], max: arr[high] };
    } else {
      return { min: arr[high], max: arr[low] };
    }
  }

  const mid = Math.floor((low + high) / 2);
  const left = divideAndConquer(arr, low, mid, counter);
  const right = divideAndConquer(arr, mid + 1, high, counter);

  // dua komparasi untuk menggabungkan min dan max
  counter.count++;
  const min = left.min < right.min ? left.min : right.min;

  counter.count++;
  const max = left.max > right.max ? left.max : right.max;

  return { min, max };
}

function dac(arr) {
  const counter = { count: 0 };
  const result = divideAndConquer(arr, 0, arr.length - 1, counter);
  return { ...result, comparisons: counter.count };
}

// Ukuran array yang akan diuji
const sizes = [1000, 10000, 100000, 1000000, 10000000];
const results = [];

for (const N of sizes) {
  // Generate array acak
  const arr = Array.from({ length: N }, () =>
    Math.floor(Math.random() * 10000000)
  );

  const bf = bruteForce(arr);
  const dnq = dac(arr);

  results.push({
    N,
    algo_BF: bf.comparisons,
    algo_DNQ: dnq.comparisons,
  });
}

console.table(results);
