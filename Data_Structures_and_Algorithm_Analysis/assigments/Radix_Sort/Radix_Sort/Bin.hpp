//
//  Bin.hpp
//  Radix_Sort
//
//  Created by Tyree Stevenson on 4/8/17.
//  Copyright © 2017 Tyree Stevenson. All rights reserved.
//

#ifndef Bin_hpp
#define Bin_hpp

#include <stdio.h>
#include "constants.h"

class Bin
{
public:
    
    Bin();
    void Append(int item);
    int Delete();
    int Size();
    bool Is_Full();
    bool Is_Empty();

private:
    
    struct Bin_Node
    {
        int number;
        Bin_Node *next = nullptr;
    };
    
    Bin_Node *head;
    int size;
};
#endif /* Bin_hpp */
