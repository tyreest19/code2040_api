//
//  main.cpp
//  Radix_Sort
//
//  Created by Tyree Stevenson on 4/7/17.
//  Copyright © 2017 Tyree Stevenson. All rights reserved.
//

#include <iostream>
#include "Utility.hpp"
#include "constants.h"
using namespace std;



int main(int argc, const char * argv[]) {
    int numbers[MAX_CONSTANT];
    int amount_of_numbers = Store_Numbers_Into_Array(numbers, FILE_NAME);
    for (int i = 0; i < amount_of_numbers; i++)
    {
        cout << numbers[i] << endl;
    }
    cout << "-------------Radix Sort------------------" << endl;
    Radix_Sort(numbers, amount_of_numbers);
    for (int i = 0; i < amount_of_numbers; i++)
    {
        cout << numbers[i] << endl;
    }
    return 0;
}

