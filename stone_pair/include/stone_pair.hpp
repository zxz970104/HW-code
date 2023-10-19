#ifndef _STONE_HPP
#define _STONE_HPP
#include <vector>
#include <unordered_map>
#include <cmath>

/// @brief retrieves two numbers from an array, and their difference is exactly D with a precision of 1e-3.
/// @param stones_weight  an array of floating-point numbers in the range [0.0,10^6].
/// @param target_diff the target difference D.
/// @return If find two numbers that meet the function's requirements, return them; otherwise, return -1.0 and -1.0.
std::pair<double, double> find_stone_pair(const std::vector<double>& stones_weight, const double target_diff) {
    std::pair<double, double> stone_pair(-1.0, -1.0); // result
    if (target_diff < 0 || target_diff > 1e6 || stones_weight.size() == 0) {
        return stone_pair;
    }
    
    // A hash table is used to store each number along with its associated precision version.
    std::unordered_map<double, double> stones_map; 
    for (size_t i = 0; i < stones_weight.size(); i++) {
        // discard error value
        if (stones_weight[i] < 0 || stones_weight[i] > 1e6) {
            continue;
        }
        double eps_weight = (std::floor(stones_weight[i] * 1e3)) / 1e3;  // adapt precision
        stones_map[eps_weight] = stones_weight[i];
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
        if (stones_map.find(eps_weight + eps_target_diff) != stones_map.end()) {
            stone_pair.first = stones_map[eps_weight + eps_target_diff];
            stone_pair.second = stones_weight[i];
            break;
        }
    }

    return stone_pair;
}

#endif