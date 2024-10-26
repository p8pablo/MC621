#include <bits/stdc++.h>
using namespace std;

struct circle {
    double cx, cy;
    double radius;
};

int dfs(int node, vector<vector<int>>& adjMatrix, vector<bool>& visited) {
    visited[node] = true;
    int componentSize = 1;

    for (int i = 0; i < adjMatrix.size(); i++) {
        if (adjMatrix[node][i] == 1 && !visited[i]) {
            componentSize += dfs(i, adjMatrix, visited);
        }
    }
    return componentSize;
}

int findLargestComponent(vector<vector<int>>& adjMatrix) {
    int n = adjMatrix.size();
    vector<bool> visited(n, false);
    int largestComponentSize = 0;

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            int componentSize = dfs(i, adjMatrix, visited);
            largestComponentSize = max(largestComponentSize, componentSize);
        }
    }
    return largestComponentSize;
}

vector<vector<int>> construct_graph(const vector<circle>& circulos) {
    int n = circulos.size();
    vector<vector<int>> matrix(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            circle c1 = circulos[i];
            circle c2 = circulos[j];
            double dx = c1.cx - c2.cx;
            double dy = c1.cy - c2.cy;
            double distSq = dx * dx + dy * dy;
            double radiusSum = c1.radius + c2.radius;
            double radiusSumSq = radiusSum * radiusSum;

            if (distSq < radiusSumSq) {  // Changed from '<' to '<='
                matrix[i][j] = 1;
                matrix[j][i] = 1;
            }
        }
    }
    return matrix;
}

int main() {
    while (true) {
        int n;
        cin >> n;
        if (n == -1) break;

        vector<circle> circulos;
        for (int i = 0; i < n; i++) {
            circle circulo;
            cin >> circulo.cx >> circulo.cy >> circulo.radius;
            circulos.push_back(circulo);
        }

        vector<vector<int>> adjMatrix = construct_graph(circulos);
        int max_comp = findLargestComponent(adjMatrix);

        if (max_comp == 1) {
            cout << "The largest component contains " << max_comp << " ring." << endl;
        } else {
            cout << "The largest component contains " << max_comp << " rings." << endl;
        }
    }
    return 0;
}
