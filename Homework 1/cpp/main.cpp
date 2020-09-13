#include <iostream>
#include <cmath>


int main() {
    int N;
    int X;
    std::cin >> N >> X;
    int *variables = new int[N];
    for (int i = 0; i < N; ++i) {
        variables[i] = 0;
        std::cin >> variables[i];
    }
    int min_list[3] = {variables[0], variables[1], variables[2]};
    double min_dif = std::fabs (X - variables[0] - variables[1] - variables[2]);

    int count = 0;
    int spec_count = 0;
    for(int i = 0; i<N;i++){
        for(int j = i+1; j<N; j++){
            if((i != j)) {
                for (int k = j+1; k < N; k++) {
                    spec_count += 1;
                    if ((i != k) && (j != k)) {
                        double dif = std::fabs(X - variables[i] - variables[j] - variables[k]);
                        count += 1;
                        if (min_dif > dif) {
                            min_dif = dif;
                            min_list[0] = variables[i];
                            min_list[1] = variables[j];
                            min_list[2] = variables[k];
                        }
                    }
                }
            }
        }
    }
    for(int i : min_list){
        std::cout << i << ' ';
    }
    std::cout << std::endl << count << spec_count << std::endl;
    delete [] variables;
    return 0;
}
