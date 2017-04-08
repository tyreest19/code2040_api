//
//  Bin.cpp
//  Radix_Sort
//
//  Created by Tyree Stevenson on 4/8/17.
//  Copyright © 2017 Tyree Stevenson. All rights reserved.
//

#include "Bin.hpp"
#include <iostream>

using namespace std;
Bin:: Bin()
{
    head = nullptr;
    size = 0;
}

void Bin:: Append(int item)
{
    Bin_Node *new_node = new Bin_Node;
    new_node->number = item;
    new_node->next = head;
    head = new_node;
    size++;
}

int Bin:: Delete()
{
    size--;
    int temp = head->number;
    head = head->next;
    return temp;
}

int Bin:: Size()
{
    return size;
}

bool Bin:: Is_Full()
{
    return false;
}

bool Bin:: Is_Empty()
{
    return size == 0 && head == nullptr;
}
