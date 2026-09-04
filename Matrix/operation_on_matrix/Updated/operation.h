#ifndef EIGEN_OPERATION_H
#define EIGEN_OPERATION_H

#include <vector>
#include <string>
using std::vector, std::string;

extern vector<vector<float>> a;
extern vector<vector<float>> b;

class matrixTools {
public:
    static vector<float> columnTraversal(vector<vector<float> >& S);
    static vector<size_t> dimensionCalculator(vector<vector<float>>& S);
};

#endif //EIGEN_OPERATION_H
