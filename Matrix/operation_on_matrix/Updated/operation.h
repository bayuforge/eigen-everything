#ifndef EIGEN_OPERATION_H
#define EIGEN_OPERATION_H

#include <vector>
using std::vector;

extern vector<vector<float>> a;
extern vector<vector<float>> b;

class matrixTools {
private:
    vector<vector<float>> a;

public:
    matrixTools(vector<vector<float>>& S) {};

    vector<float> columnTraversal(vector<vector<float> >& S);
    int dimensionCalculator(vector<vector<float>>& S);
};

#endif //EIGEN_OPERATION_H
