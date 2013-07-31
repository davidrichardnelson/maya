#ifndef __KD_TREEM
#define __KD_TREEM

#include <maya/MPointArray.h>
#include <kdTree.h>

//template<typename ExtraInfo>
KdTree_map<int> KdFromPointArray(MPointArray &points)
{
    int size = points.length();
    KdTree_map<int> newKd(size);
    for (int i=0; i< size; i++)
    {
        float pos[3] = {float(points[i].x), float(points[i].y), float(points[i].z)};
        const int index = i;
        newKd.store(pos, &index);
    }
    newKd.balance();
    return newKd;

}

#endif