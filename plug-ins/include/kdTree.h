// KdTree.h
// a kd tree baised on an example implementation of the KdTree 
// map data structure (Henrik Wann Jensen - February 2001)

#ifndef __KD_TREE
#define __KD_TREE

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <maya/MGlobal.h>

// This is the KdTree
template<typename ExtraInfo>
struct KdTree {
    float pos[3];                 // KdTree position
    short plane;                  // splitting plane for kd-tree
    ExtraInfo info;               // whatever you want

    KdTree()
        : info(), plane(0)
    {
        pos[0] = 0.0f;
        pos[1] = 0.0f;
        pos[2] = 0.0f;
    }
    ExtraInfo* Info() { return &info; }
    void SetInfo(const ExtraInfo* info)
	{
        this->info = *info;
    }
};


// This structure is used only to locate the nearest points
template<typename ExtraInfo>
struct ClosestPoints {
    int max;
    int found;
    bool got_heap;
    float pos[3];
    float *dist2;
    const KdTree<ExtraInfo> **index;
};


// This is the KdTree_map class
template<typename ExtraInfo>
class KdTree_map {
public:
    KdTree_map( int maxPoints );
    ~KdTree_map();

    void store(
        const float pos[3],            // KdTree position
         const ExtraInfo* info);       // user info

    void balance(void);              // balance the kd-tree (before use!)

    int closestPoints(
        KdTree<ExtraInfo> *thePoints,
        const float pos[3],            // surface position
        const float max_dist,          // max distance to look for points in KdTrees
        const int maxPoints ) const;    // number of points to find

    void locate_points(
        ClosestPoints<ExtraInfo> *const np,      // np is used to locate the KdTrees
        const int index ) const;       // call with index = 1


private:

    void balance_segment(
        KdTree<ExtraInfo> **pbal,
        KdTree<ExtraInfo> **porg,
        const int index,
        const int start,
        const int end );

    void median_split(
        KdTree<ExtraInfo> **p,
        const int start,
        const int end,
        const int median,
        const int axis );

    KdTree<ExtraInfo> *KdTrees;

    int stored_KdTrees;
    int half_stored_KdTrees;
    int max_KdTrees;

    float bbox_min[3];		// use bbox_min;
    float bbox_max[3];		// use bbox_max;
};



// This is the constructor for the KdTree map.
// To create the KdTree map it is necessary to specify the
// maximum number of KdTrees that will be stored
template<typename ExtraInfo>
KdTree_map<ExtraInfo>::KdTree_map( const int maxPoints )
{
    stored_KdTrees = 0;
    max_KdTrees = maxPoints;

    KdTrees = new KdTree<ExtraInfo>[ max_KdTrees+1 ];

    if (KdTrees == NULL) {
        fprintf(stderr,"Out of memory initializing KdTree map\n");
        exit(-1);
    }

    bbox_min[0] = bbox_min[1] = bbox_min[2] = 1e8f;
    bbox_max[0] = bbox_max[1] = bbox_max[2] = -1e8f;
}

template<typename ExtraInfo>
KdTree_map<ExtraInfo>::~KdTree_map()
{
    delete[] KdTrees;
}


// KdTree_dir returns the direction of a KdTree
template<typename ExtraInfo>
int KdTree_map<ExtraInfo>::closestPoints( 
                                       KdTree<ExtraInfo> *thePoints,
                                       const float pos[3],             // surface position
                                       const float max_dist,           // max distance to look for KdTrees
                                       const int maxPoints ) const     // number of KdTrees to use
{
    //point[0] = point[1] = point[2] = 0.0;

    ClosestPoints<ExtraInfo> np;
    np.dist2 = (float*)alloca( sizeof(float)*(maxPoints+1) );
    np.index = (const KdTree<ExtraInfo>**)alloca( sizeof(KdTree<ExtraInfo>*)*(maxPoints+1) );

    np.pos[0] = pos[0]; np.pos[1] = pos[1]; np.pos[2] = pos[2];
    np.max = maxPoints;
    np.found = 0;
    np.got_heap = false;
    np.dist2[0] = max_dist*max_dist;
    
    // locate the nearest points
    locate_points( &np, 1 );
    if (thePoints != NULL)
    {
        int i;

        float *distances = new float[np.found];
        for (i = 0; i < np.found; i++)
        {
            distances[i] = np.dist2[i+1];
        }
        for (i = 0; i < np.found; i++)
        {
            float dist2 = distances[i];
            KdTree<ExtraInfo> tempNode = *np.index[i+1];
            int j = i;
            while (j > 0 && distances[j - 1] > dist2)
            {
                np.index[j] = np.index[j - 1];
                distances[j] = distances[j - 1];
                j--;
            }
            thePoints[j] = tempNode;
            distances[j] = dist2;
        }
/*

        int max = min(np.found, maxPoints);
        for (i = 1; i <= np.found; i++)
        {
            thePoints[i - 1] = *np.index[i];
        }
*/
    }

    return np.found;
}


// locate_points finds the nearest KdTrees in the
// KdTree map given the parameters in np
template<typename ExtraInfo>
void KdTree_map<ExtraInfo>::locate_points(
                                  ClosestPoints<ExtraInfo> *const np,
                                  const int index ) const
{
    const KdTree<ExtraInfo> *p = &KdTrees[index];
    float dist1;


    if (index<=half_stored_KdTrees) {
        dist1 = np->pos[ p->plane ] - p->pos[ p->plane ];
        int leftIndex = index * 2;
		int rightIndex = leftIndex + 1;
        if (dist1>=0.0) { // if dist1 is positive search right plane
            if (rightIndex <= stored_KdTrees)
                locate_points( np, rightIndex );
            if ( dist1*dist1 < np->dist2[0] )
                locate_points( np, leftIndex );
        } else {         // dist1 is negative search left first
            locate_points( np, leftIndex );
            if ( dist1*dist1 < np->dist2[0]  && rightIndex <= stored_KdTrees)
                locate_points( np, rightIndex );
        }
    }
    // compute squared distance between current point and np->pos

    dist1 = p->pos[0] - np->pos[0];
    float dist2 = dist1*dist1;
    dist1 = p->pos[1] - np->pos[1];
    dist2 += dist1*dist1;
    dist1 = p->pos[2] - np->pos[2];
    dist2 += dist1*dist1;

    if ( dist2 < np->dist2[0] ) {
        // we found a point :) Insert it in the candidate list

        if ( np->found < np->max ) {
            // heap is not full; use array
            np->found++;
            np->dist2[np->found] = dist2;
            np->index[np->found] = p;
        } else {
            int j,parent;

            if (np->got_heap==false) { // Do we need to build the heap?
                // Build heap
                float dst2;
                const KdTree<ExtraInfo> *phot;
                int half_found = np->found>>1;
                for ( int k=half_found; k>=1; k--) {
                    parent=k;
                    phot = np->index[k];
                    dst2 = np->dist2[k];
                    while ( parent <= half_found ) {
                        j = parent+parent;
                        if (j<np->found && np->dist2[j]<np->dist2[j+1])
                            j++;
                        if (dst2>=np->dist2[j])
                            break;
                        np->dist2[parent] = np->dist2[j];
                        np->index[parent] = np->index[j];
                        parent=j;
                    }
                    np->dist2[parent] = dst2;
                    np->index[parent] = phot;
                }
                np->got_heap = 1;
            }

            // insert new point into max heap
            // delete largest element, insert new and reorder the heap
            parent=1;
            j = 2;
            while ( j <= np->found ) {
                if ( j < np->found && np->dist2[j] < np->dist2[j+1] )
                    j++;
                if ( dist2 > np->dist2[j] )
                    break;
                np->dist2[parent] = np->dist2[j];
                np->index[parent] = np->index[j];
                parent = j;
                j += j;
            }
            if (dist2 < np->dist2[parent]) {
			    np->index[parent] = p;
			    np->dist2[parent] = dist2;
		    }

            np->dist2[0] = np->dist2[1];
        }
    }
}


// store puts a KdTree into the flat array that will form
//the final kd-tree.
//Call this function to store a KdTree.
template<typename ExtraInfo>
void KdTree_map<ExtraInfo>::store(
                         const float pos[3],
                         const ExtraInfo *info)
{
    if (stored_KdTrees>=max_KdTrees)
        return;

    stored_KdTrees++;
    KdTree<ExtraInfo> *const node = &KdTrees[stored_KdTrees];

    for (int i=0; i<3; i++) {
        node->pos[i] = pos[i];

        if (node->pos[i] < bbox_min[i])
            bbox_min[i] = node->pos[i];
        if (node->pos[i] > bbox_max[i])
            bbox_max[i] = node->pos[i];

    }
    node->SetInfo(info);

}


// balance creates a left balanced kd-tree from the flat KdTree array.
//This function should be called before the KdTree map
// is used for rendering.
template<typename ExtraInfo>
void KdTree_map<ExtraInfo>::balance(void)
{
    if (stored_KdTrees>1) {
        // allocate two temporary arrays for the balancing procedure
        KdTree<ExtraInfo> **pa1 = new KdTree<ExtraInfo>*[stored_KdTrees+1];
        KdTree<ExtraInfo> **pa2 = new KdTree<ExtraInfo>*[stored_KdTrees+1];

        for (int i=0; i<=stored_KdTrees; i++){
            pa2[i] = &KdTrees[i];
        }

        balance_segment( pa1, pa2, 1, 1, stored_KdTrees );
        delete[] pa2;

        // reorganize balanced kd-tree (make a heap)
        int d, j=1, foo=1;
        KdTree<ExtraInfo> foo_KdTree = KdTrees[j];

        for (int i=1; i<=stored_KdTrees; i++) {
            d=pa1[j]-KdTrees;
            //d = (((unsigned long)pa1[j]) - ((unsigned long)KdTrees)) /
			//			sizeof(KdTrees<ExtraInfo>);
            pa1[j] = NULL;
            if (d != foo)
            {
                KdTrees[j] = KdTrees[d];
            }
            else {
                KdTrees[j] = foo_KdTree;
                if (i<stored_KdTrees) {
                    for (;foo<=stored_KdTrees; foo++){
                        if (pa1[foo] != NULL)
                            break;
                    }
                    foo_KdTree = KdTrees[foo];
                    j = foo;
                }

                continue;
            }
            j = d;
        }
        delete[] pa1;
    }

    half_stored_KdTrees = stored_KdTrees/2;
}


//#define swap(ph,a,b) { KdTree *ph2=ph[a]; ph[a]=ph[b]; ph[b]=ph2; }

// median_split splits the KdTree array into two separate
// pieces around the median with all KdTrees below the
// the median in the lower half and all KdTrees above
// than the median in the upper half. The comparison
// criteria is the axis (indicated by the axis parameter)
// (inspired by routine in "Algorithms in C++" by Sedgewick)
template<typename ExtraInfo>
void KdTree_map<ExtraInfo> :: median_split(
                                KdTree<ExtraInfo> **p,
                                const int start,               // start of KdTree block in array
                                const int end,                 // end of KdTree block in array
                                const int median,              // desired median number
                                const int axis )               // axis to split along
{
    int left = start;
    int right = end;

    while ( right > left ) {
        const float v = p[right]->pos[axis];
        int i=left-1;
        int j=right;
        for (;;) {
            while ( p[++i]->pos[axis] < v )
                ;
            while ( p[--j]->pos[axis] > v && j>left )
                ;
            if ( i >= j )
                break;
            //swap(p,i,j);
            KdTree<ExtraInfo> *ph2 = p[i];
			p[i] = p[j];
			p[j] = ph2;
        }

        KdTree<ExtraInfo> *ph2 = p[i];
		p[i] = p[right];
		p[right] = ph2;
        //swap(p,i,right);
        if ( i >= median )
            right=i-1;
        if ( i <= median )
            left=i+1;
    }


}


// See "Realistic image synthesis using KdTree Mapping" chapter 6
// for an explanation of this function
template<typename ExtraInfo>
void KdTree_map<ExtraInfo> :: balance_segment(
                                   KdTree<ExtraInfo> **pbal,
                                   KdTree<ExtraInfo> **porg,
                                   const int index,
                                   const int start,
                                   const int end )
{
    //--------------------
    // compute new median
    //--------------------

    int median=1;
    while ((4*median) <= (end-start+1))
        median += median;

    if ((3*median) <= (end-start+1)) {
        median += median;
        median += start-1;
    } else	
        median = end-median+1;

    //--------------------------
    // find axis to split along
    //--------------------------

    int axis=2;
    if ((bbox_max[0]-bbox_min[0])>(bbox_max[1]-bbox_min[1]) &&
        (bbox_max[0]-bbox_min[0])>(bbox_max[2]-bbox_min[2]))
        axis=0;
    else if ((bbox_max[1]-bbox_min[1])>(bbox_max[2]-bbox_min[2]))
        axis=1;

    //------------------------------------------
    // partition KdTree block around the median
    //------------------------------------------

    median_split( porg, start, end, median, axis );

    pbal[ index ] = porg[ median ];
    pbal[ index ]->plane = axis;

    //----------------------------------------------
    // recursively balance the left and right block
    //----------------------------------------------

    if ( median > start ) {
        // balance left segment
        if ( start < median-1 ) {
            const float tmp=bbox_max[axis];
            bbox_max[axis] = pbal[index]->pos[axis];
            balance_segment( pbal, porg, 2*index, start, median-1 );
            bbox_max[axis] = tmp;
        } else {
            pbal[ 2*index ] = porg[start];
        }
    }

    if ( median < end ) {
        // balance right segment
        if ( median+1 < end ) {
            const float tmp = bbox_min[axis];		
            bbox_min[axis] = pbal[index]->pos[axis];
            balance_segment( pbal, porg, 2*index+1, median+1, end );
            bbox_min[axis] = tmp;
        } else {
            pbal[ 2*index+1 ] = porg[end];
        }
    }	
}

#endif
