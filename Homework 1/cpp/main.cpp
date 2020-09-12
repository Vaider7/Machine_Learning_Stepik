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
    int min_list[3];
    double min_dif = std::fabs (X - variables[0] - variables[1] - variables[2]);
    for(int i = 0; i<N;i++){
        for(int j=0; j<N; j++){
            for(int k=0; k<N; k++){
                if((i != j)&&(i != k)&&(j != k)){
                    double dif = std::fabs (X - variables[i] - variables[j] - variables[k]);
                    if(min_dif>dif){
                        min_dif = dif;
                        min_list[0] = variables[i];
                        min_list[1] = variables[j];
                        min_list[2] = variables[k];
                    }
                }
            }
        }
    }
    for(int i : min_list){
        std::cout << i << ' ';
    }
    delete [] variables;
    return 0;
}
