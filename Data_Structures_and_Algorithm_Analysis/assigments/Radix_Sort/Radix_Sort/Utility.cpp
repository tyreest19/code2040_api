//
//  Utility.cpp
//  Radix_Sort
//
//  Created by Tyree Stevenson on 4/7/17.
//  Copyright © 2017 Tyree Stevenson. All rights reserved.
//

#include <string>
#include <iostream>
#include <fstream>
#include "Utility.hpp"
#include "Bin.hpp"
using namespace std;

//==========================================================================================
// Takes constant char pointer and converts it into a string.
// If one of the characters are not a digit the function returns -1.
//==========================================================================================
int String_To_Int(const char *str)
{
    int result = 0;
    int prefix = 0;
    
    if (str[0] == '\0')
    {
        return -1;
    }
    
    else if (str[0] == '-' || str[0] == '+')
    {
        prefix = 1;
    }
    
    for (int i = prefix; str[i] != '\0'; ++i)
    {
        if ('0' <= str[i] && str[i] <= '9')
        {
            result = result*10 + str[i] - '0';
        }
        
        else
        {
            return -1;
        }
    }
    
    if (str[0] == '-')
    {
        result *= -1;
    }
    
    return result;
}

//==========================================================================================
// Stores numbers from text file into an array
// Returns the amount of numbers
//==========================================================================================

int Store_Numbers_Into_Array(int array[], string file_name)
{
    ifstream file;
    file.open(file_name);
    int count = 0;
    int number;
    while (file >> number)
    {
        array[count] = number;
        count++;
    }
    file.close();
    return count;
}

//==========================================================================================
// Stores numbers by siginficant digits
//=========================================================================================

void Radix_Sort(int array[], int amount_of_numbers)
{
    Bin bins[NUMBER_OF_BINS + 1];
}
