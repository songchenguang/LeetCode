//
//  MaxmumSubArray.cpp
//  LeetCode_CPP
//
//  Created by carlcgsong on 2020/11/14.
//  Copyright © 2020 chenguang. All rights reserved.
//

#include "MaxmumSubArray.hpp"

int Solution::maxSubArray(vector<int> &nums) {
    int maxSum = nums.at(0);
    for (int startIndex = 0; startIndex < nums.size(); startIndex++) {
        int currentSum = nums.at(startIndex);
        if (currentSum > maxSum) {
            maxSum = currentSum;
        }
        for (int index = startIndex + 1; index < nums.size(); index++) {
            currentSum = currentSum + nums.at(index);
            if (currentSum > maxSum) {
                maxSum = currentSum;
            }
        }
    }
    return maxSum;
}
