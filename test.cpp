#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include "stone_pair.hpp"

void displayUsage(const std::string& programName) {
    std::cerr << "Usage: " << programName << " <TXT file>" << std::endl;
}

std::vector<double> split(const std::string& str, char delimiter) {
    std::vector<double> tokens;
    size_t pos = 0;
    size_t found = 0;
    while ((found = str.find(delimiter, pos)) != std::string::npos) {
        tokens.push_back(std::stod(str.substr(pos,found - pos)));
        pos = found + 1;
    }

    tokens.push_back(std::stod(str.substr(pos)));
    return tokens;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        displayUsage(argv[0]);
        return 1;
    }

    const std::string fileName = argv[1];

    std::ifstream file(fileName);

    if (!file.is_open()) {
        std::cerr << "Unable to open TXT file: " << fileName << std::endl;
        return 1;
    }

    std::vector<double> data; 

    std::string line;
    unsigned int count = 0;
    unsigned int success = 0;
    while (std::getline(file, line)) {
        count++;
        if (line[0] != '1') {
            continue;
        }
        std::vector<double> data = split(line, ',');
        double D = data[1];
        std::pair<int, int> except(data[2], data[3]);

        std::vector<double> stone_weight(data.begin() + 4, data.end()); 

        std::pair<int, int> stone_pair = find_stone_pair(stone_weight, D); // Find the stone pair
        if ((stone_pair.first == except.first && stone_pair.second == except.second)
            || stone_pair.first == except.second && stone_pair.second == except.first) {
            std::cout << count << " OK" << std::endl; 
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