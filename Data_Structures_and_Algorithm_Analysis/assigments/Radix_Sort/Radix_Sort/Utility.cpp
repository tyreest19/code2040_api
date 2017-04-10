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

void Radix_Sort(int array[], int n)
{
    // Find the maximum number to know number of digits
    int m = Find_Largest_Number(array, n);
    
    // Do counting sort for every digit. Note that instead
    // of passing digit number, exp is passed. exp is 10^i
    // where i is current digit number
    for (int exp = 1; m/exp > 0; exp *= 10)
        Count_Sort(array, n, exp);
}

//=========================================================================================
// Get max number
//=========================================================================================

int Find_Largest_Number(int array[], int amount_of_numbers)
{
    int largest_number = array[0];
    for (int i = 1; i < amount_of_numbers; i++)
        if (array[i] > largest_number)
            largest_number = array[i];
    return largest_number;
}

void Count_Sort(int array[], int amount_of_numbers, int exp)
{
    int output[amount_of_numbers]; // output array
    int i, count[10] = {0};
    
    // Store count of occurrences in count[]
    for (i = 0; i < amount_of_numbers; i++)
        count[ (array[i]/exp)%10 ]++;
    
    // Change count[i] so that count[i] now contains actual
    //  position of this digit in output[]
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];
    
    // Build the output array
    for (i = amount_of_numbers - 1; i >= 0; i--)
    {
        output[count[ (array[i]/exp)%10 ] - 1] = array[i];
        count[ (array[i]/exp)%10 ]--;
    }
    
    // Copy the output array to arr[], so that arr[] now
    // contains sorted numbers according to current digit
    for (i = 0; i < amount_of_numbers; i++)
        array[i] = output[i];
}
