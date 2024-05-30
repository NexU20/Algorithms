class Graph {
  constructor() {
    this.nodes = new Set();
    this.edges = {};
  }

  addNode(node) {
    this.nodes.add(node);
    this.edges[node] = [];
  }

  addEdge(node1, node2, weight) {
    this.edges[node1].push({ node: node2, weight: weight });
    this.edges[node2].push({ node: node1, weight: weight });
  }
}

function dijkstra(graph, startNode, endNode) {
  const distances = {};
  const previousNodes = {};
  const visited = {};
  const queue = new PriorityQueue();

  // Initialize distances and visited flags
  for (const node of graph.nodes) {
    distances[node] = Infinity;
    visited[node] = false;
    previousNodes[node] = null;
  }

  distances[startNode] = 0;
  queue.enqueue(startNode, 0);

  while (!queue.isEmpty()) {
    const currentNode = queue.dequeue().element;

    if (currentNode === endNode) {
      // Found the shortest path to the end node
      const path = [];
      let current = currentNode;

      while (current !== null) {
        path.unshift(current);
        current = previousNodes[current];
      }

      return { distance: distances[endNode], path };
    }

    if (visited[currentNode]) continue;

    visited[currentNode] = true;

    for (const neighbor of graph.edges[currentNode]) {
      const { node, weight } = neighbor;
      const distanceToNeighbor = distances[currentNode] + weight;

      if (distanceToNeighbor < distances[node]) {
        distances[node] = distanceToNeighbor;
        previousNodes[node] = currentNode;
        queue.enqueue(node, distanceToNeighbor);
      }
    }
  }

  // No path found to the end node
  return { distance: Infinity, path: [] };
}

class PriorityQueue {
  constructor() {
    this.queue = [];
  }

  enqueue(element, priority) {
    const item = { element, priority };
    let added = false;

    for (let i = 0; i < this.queue.length; i++) {
      if (item.priority < this.queue[i].priority) {
        this.queue.splice(i, 0, item);
        added = true;
        break;
      }
    }

    if (!added) {
      this.queue.push(item);
    }
  }

  dequeue() {
    return this.queue.shift();
  }

  isEmpty() {
    return this.queue.length === 0;
  }
}

// Example usage
const graph = new Graph();
for (let i = 1; i <= 16; i++) {
  graph.addNode(i);
}

graph.addEdge(1, 2, 67);
graph.addEdge(1, 16, 203);

graph.addEdge(2, 3, 108);

graph.addEdge(3, 4, 92);
graph.addEdge(3, 15, 120);

graph.addEdge(4, 5, 82);
graph.addEdge(4, 9, 47);

graph.addEdge(5, 6, 40);

graph.addEdge(6, 7, 62);
graph.addEdge(6, 10, 66.5);

graph.addEdge(7, 8, 49);

graph.addEdge(8, 9, 28);
graph.addEdge(8, 14, 62);

graph.addEdge(10, 11, 71);

graph.addEdge(11, 12, 47);

graph.addEdge(12, 13, 181.5);

graph.addEdge(13, 14, 45.5);

graph.addEdge(14, 8, 62);
graph.addEdge(14, 15, 95);

graph.addEdge(15, 16, 111);

const startNode = 1;
const endNode = 9;

const result = dijkstra(graph, startNode, endNode);

if (result.distance !== Infinity) {
  console.log(result.distance + "m");
  console.log("Shortest path:", result.path.join(" -> "));
} else {
  console.log("No path found from node", startNode, "to", endNode);
}

// for (const node in graph.edges) {
//   console.log(`Tetangga dari ${node} berjumlah: ${graph.edges[node].length}`);
// }
