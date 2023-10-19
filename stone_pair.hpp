#ifndef _STONE_HPP
#define _STONE_HPP
#include <vector>
#include <unordered_map>
#include <cmath>

/// @brief retrieves two numbers from an array, and their difference is exactly D with a precision of 1e-3.
/// @param stones_weight  an array of floating-point numbers in the range [0.0,10^6].
/// @param target_diff the target difference D.
/// @return If find two numbers that meet the function's requirements, return their index; otherwise, return -1 and -1.
std::pair<int, int> find_stone_pair(const std::vector<double>& stones_weight, const double target_diff) {
    std::pair<int, int> stone_pair(-1, -1); // result
    if (target_diff < 0 || target_diff > 1e6 || stones_weight.size() == 0) {
        return stone_pair;
    }
    
    // A hash table is used to store each number along with its associated precision version.
    std::unordered_map<double, int> stones_map; 
    for (size_t i = 0; i < stones_weight.size(); i++) {
        // discard error value
        if (stones_weight[i] < 0 || stones_weight[i] > 1e6) {
            continue;
        }
        double eps_weight = (std::floor(stones_weight[i] * 1e3)) / 1e3;  // adapt precision
        stones_map[eps_weight] = i;
    }

    double eps_target_diff = (std::floor(target_diff * 1e3)) / 1e3; // adapt precision
    for (size_t i = 0; i < stones_weight.size(); i++) {
        if (stones_weight[i] < 0 || stones_weight[i] > 1e6) {
            continue;
        }
        double eps_weight = (std::floor(stones_weight[i] * 1e3)) / 1e3;  // adapt precision
        /*
        for each number, calculate the sum of the target value and current value, 
        and then check in the map whether this sum already exists. 
        If it does, it indicates that a combination of two numbers has been found.
        */
        double key = std::floor((eps_weight + eps_target_diff) * 1e3) / 1e3;
        if (stones_map.find(key) != stones_map.end()) {
            if (i != stones_map[key]) {
                stone_pair.first = stones_map[key];
                stone_pair.second = i;
                break;
            }
        }
    }

    return stone_pair;
}



#endif