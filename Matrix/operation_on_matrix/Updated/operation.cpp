#include <iostream>
#include "operation.h"
using std::cout;

void do_column_traversal(vector<vector<float>>& S);
void do_dimension_calculator(vector<vector<float>>& S);

int main() {
    // examples of both a and b matrix
    vector<vector<float>> a;
    vector<vector<float>> b;

    // try these operation first
    do_column_traversal(a);
    do_dimension_calculator(b);

    return 0;
}

void do_column_traversal(vector<vector<float>> &S) {
    vector<float> response = matrixTools::columnTraversal(S);

    cout << "col traversal completed";
    for (int i = 0; i < response.size(); i++) {
        cout << "col " << i << ": " << response[i] << "\n";
    }
}

void do_dimension_calculator(vector<vector<float>> &S) {
    vector<size_t> response = matrixTools::dimensionCalculator(S);
    size_t row_count = response[0];
    size_t column_count = response[1];

    cout << "dimension calculator completed";
    cout << "row count: " << row_count;
    cout << "col count: " << column_count;
}
