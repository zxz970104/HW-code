#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include "stone_pair2.hpp"

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
        int pair_num = data[2];
        int possible_res_count = data[3];
        std::vector<std::set<std::pair<int, int>>> cadidate;
        for (int k = 0; k < possible_res_count; k++) {
            std::set<std::pair<int, int>> tmp;
            for (int i = 4 + k * pair_num * 2; i < pair_num * (k+1) * 2  + 4; i += 2) {
                tmp.insert(std::make_pair(data[i], data[i + 1]));
                tmp.insert(std::make_pair(data[i + 1], data[i]));
            }
            cadidate.push_back(tmp);
        }
        // std::cout << "==============" << std::endl;
        // for (auto& item: cadidate) {
        //     for (auto& pair : item) {
        //         std::cout << pair.first << "," << pair.second << ";";
        //     }
        //     std::cout << std::endl;
        // }
        std::vector<double> stone_weight(data.begin() + pair_num * possible_res_count * 2  + 4, data.end());
        std::vector<std::pair<int, int>> stone_pair = find_all_stone_pairs(stone_weight, D); // Find the stone pair


        bool succ = false;
        std::vector<std::pair<int, int>> err_pairs;
        if (stone_pair.size() == pair_num && pair_num == 0) {
            std::cout << count << " OK" <<  std::endl; 
            success++;
            succ = true;
        } else if (stone_pair.size() != pair_num) {
            std::cerr << count << " ERROR :" << pair_num  << " pairs are expected, but " << stone_pair.size() << " pairs are found." << std::endl;
        } else {
            for(auto& pairs : cadidate) {
                for (auto& item : stone_pair) {
                    if (pairs.find(item) != pairs.end()) {
                        pair_num--;
                        pairs.erase(item);
                    } else {
                        err_pairs.push_back(item);
                    }
                    
                }
                if (pair_num == 0) {
                    std::cout << count << " OK" <<  std::endl; 
                    success++;
                    succ = true;
                    break;
                } 
            }
        }

        if (!succ) {
            std::cerr << count << " ERROR :" 
            << "the pair [";
            for (auto& item : err_pairs) {
                std::cout << "(" << item.first << "," << item.second << ");";
            }
            std::cout << "] is not in the candidate." << std::endl;
        }

        
        
        data.clear();

    }
    std::cout << "Total cases: " << count << std::endl;
    std::cout << "Success cases: " << success << std::endl;
    std::cout << "error cases: " << count - success << std::endl;
    file.close();
    return 0;
}