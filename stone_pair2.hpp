#ifndef _STONE_2_HPP
#define _STONE_2_HPP
#include <vector>
#include <unordered_map>
#include <cmath>
#include <set>

/// @brief find all stone pairs from an array, 
///        and the difference between the two numbers in any pair is exactly D ( D ∈ [0.0, 10^6] ) with a precision of 1e-3.
///        Each number can be used only once
/// @param stones_weight  an array of floating-point numbers in the range [0.0,10^6].
/// @param target_diff the target difference D.
/// @return pairs that meet the function's requirements or empty vector.
std::vector<std::pair<int, int>> find_all_stone_pairs(const std::vector<double>& stones_weight, const double target_diff) {
    std::vector<std::pair<int, int>> result;
    if (target_diff < 0 || target_diff > 1e6 || stones_weight.size() == 0) {
        return result;
    }
    
    // A hash table is used to store each number along with its associated precision version.
    std::unordered_map<double, std::vector<int>> stones_map; 
    for (int i = 0; i < stones_weight.size(); i++) {
        // discard error value
        if (stones_weight[i] < 0 || stones_weight[i] > 1e6) {
            continue;
        }
        double eps_weight = (std::floor(stones_weight[i] * 1e3)) / 1e3;  // adapt precision
        if (stones_map.find(eps_weight) == stones_map.end()) {
            stones_map[eps_weight] = { i };
        } else {
            stones_map[eps_weight].push_back(i);
        }
        
    }

    std::vector<bool> used(stones_weight.size(), false);
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
            if (stones_map[key].empty()) {
                continue;
            }
            int j = stones_map[key].back();
            if (i == j) {
                continue;
            }
            stones_map[key].pop_back();
            if (used[i] || used[j]) {
                continue;
            }
            
            std::pair<int, int> pair1 = std::make_pair(i, j);
            result.push_back(pair1);
            used[i] = true;
            used[j] = true;

        }
    }


    return result;
}


#endif