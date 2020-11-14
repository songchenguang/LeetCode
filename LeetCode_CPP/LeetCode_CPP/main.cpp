//
//  main.cpp
//  LeetCode_CPP
//
//  Created by 宋晨光 on 2020/9/12.
//  Copyright © 2020 chenguang. All rights reserved.
//

#include <iostream>
#include "MaxmumSubArray.hpp"

int main(int argc, const char * argv[]) {
    std::cout << "Hello, World!\n";
    Solution solution;
    vector<int> list = {-2,1,-3,4,-1,2,1,-5,4};
    std::cout << solution.maxSubArray(list) << endl;
    
    
    return 0;
}
