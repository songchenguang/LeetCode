//
//  TwoSum.cpp
//  LeetCode_CPP
//
//  Created by 宋晨光 on 2020/9/12.
//  Copyright © 2020 chenguang. All rights reserved.
//

#include "TwoSum.hpp"
#include <unordered_map>

//vector<int> Solution::twoSum(vector<int> &nums, int target) {
//    long n = nums.size();
//    for (int i = 0; i < n; ++i) {
//        for (int j = i + 1; j < n; ++j) {
//            if (nums[i] + nums[j] == target) {
//                return {i, j};
//            }
//        }
//    }
//    return {};
//}

vector<int> Solution::twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> hashMap;
    for (int i = 0; i < nums.size(); i++) {
        auto it = hashMap.find(target - nums.at(i));
        if (it != hashMap.end()) {
            return {it->second, i};
        }
        hashMap[nums.at(i)] = i;
    }
    return {};
}
