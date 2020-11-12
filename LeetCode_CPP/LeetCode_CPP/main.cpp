//
//  main.cpp
//  LeetCode_CPP
//
//  Created by 宋晨光 on 2020/9/12.
//  Copyright © 2020 chenguang. All rights reserved.
//

#include <iostream>
#include "TwoSum.hpp"

int main(int argc, const char * argv[]) {
    std::cout << "Hello, World!\n";
    Solution solution;
    vector<int> list = {3, 2, 4};
    for (int num : solution.twoSum(list, 6)) {
        std::cout << num << " ";
    }
    
    return 0;
}
