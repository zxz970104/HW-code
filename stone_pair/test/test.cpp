#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include "stone_pair.hpp"

void displayUsage(const std::string& programName) {
    std::cerr << "Usage: " << programName << " <CSV file>" << std::endl;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        displayUsage(argv[0]);
        return 1;
    }

    const std::string csvFileName = argv[1];

    std::ifstream file(csvFileName);

    if (!file.is_open()) {
        std::cerr << "Unable to open CSV file: " << csvFileName << std::endl;
        return 1;
    }

    std::vector<double> data; 

    std::string line;
    unsigned int count = 0;
    unsigned int success = 0;
    while (std::getline(file, line)) {
        count++;
        std::istringstream ss(line);
        double D;
        ss >> D; 

        std::pair<double,double> except;
        ss >> except.first >> except.second;

        double value;
        while (ss >> value) {
            data.push_back(value);
        }
        std::cout << D << std::endl;

        std::pair<double, double> stone_pair = find_stone_pair(data, D); // Find the stone pair
        if ((stone_pair.first == except.first && stone_pair.second == except.second)
            || stone_pair.first == except.second && stone_pair.second == except.first) {
            std::cout << count << " OK" <<  std::endl; 
            success++;
        } else {
            std::cerr << count << " ERROR :" 
            << "the expeted pair (" << except.first << "," << except.second << ") is not the same as (" 
            << stone_pair.first << "," << stone_pair.second << ")." << std::endl;
        }

        data.clear();

        
    }
    std::cout << "Total cases: " << count << std::endl;
    std::cout << "Success cases: " << success << std::endl;
    std::cout << "error cases: " << count - success << std::endl;
    file.close();
    return 0;
}