#include <iostream>
#include <fstream>
#include <cmath>

int main() 
	{ double dt;
	int nsteps;
	// open parameter file
	std::ifstream paramFile("../data/params.dat");
	if (!paramFile.is_open()){
	std::cerr << "error: could not open parameter file"<< std::endl;
		return 1;
	}

	//assign variables from file and close file
	paramFile >> dt >> nsteps;
	paramFile.close();
	
	// assign initial variables
	double x = 1.0;
	double t = 0.0;

	// open output file
	std:: ofstream outputFile("../data/output.dat");
	if (!outputFile.is_open()){ 
		std::cerr << "error: couldn't open output file" << std::endl;
		return 1;
	}

	// header in output file
	outputFile << "# t x(t)" << std::endl;

	// eulers method
	for (int i=0; i<= nsteps; ++i){
		outputFile << t << " " << x<< std::endl;
		x = (1-3*dt)*x;
		t+=dt;
	}

	outputFile.close();
	
	std::cout<< "euler's method successful and saved in output file" << std::endl;

	return 0;
}
