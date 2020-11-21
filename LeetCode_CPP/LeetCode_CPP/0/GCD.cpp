//
//  GCD.cpp
//  LeetCode_CPP
//
//  Created by carlcgsong on 2020/11/21.
//  Copyright © 2020 chenguang. All rights reserved.
//

#include "GCD.hpp"

int Solution::gcd(int num1, int num2) {
    if (num2 > num1) {
        int temp = num1;
        num1 = num2;
        num2 = temp;
    }
    
    while (num2 != 0) {
        int temp = num1 % num2;
        num1 = num2;
        num2 = temp;
    }
    return num1;
}
