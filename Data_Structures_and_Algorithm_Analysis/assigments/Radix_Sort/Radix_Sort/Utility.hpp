//
//  Utility.hpp
//  Radix_Sort
//
//  Created by Tyree Stevenson on 4/7/17.
//  Copyright © 2017 Tyree Stevenson. All rights reserved.
//

#ifndef Utility_hpp
#define Utility_hpp

#include <stdio.h>
#include <string>
#include "Bin.hpp"
int Store_Numbers_Into_Array(int array[], std::string file_name);
int String_To_Int(const char *str);
void Radix_Sort(int array[], int amount_of_numbers);
int Find_Largest_Number(int array[], int amount_of_numbers);
void Count_Sort(int array[], int amount_of_numbers, int exp);
#endif /* Utility_hpp */
