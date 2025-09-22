#include <iostream>
#include <fstream>
#include <cmath>

int main() {
    double dt;
    int nsteps;
    std::ifstream params("params.dat");
    if(!params) {
        std::cerr << "Could not open params.dat\n";
        return 1;
    }
    params >> dt >> nsteps;

    std::ofstream out("output.dat");
    double x = 1.0;
    double t = 0.0;
    for(int i=0; i<nsteps; ++i) {
        out << t << " " << x << "\n";
        x = (1 - 3*dt)*x;
        t += dt;
    }
    return 0;
}

