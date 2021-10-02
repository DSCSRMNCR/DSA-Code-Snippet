#problem link - https://www.hackerrank.com/challenges/picking-numbers/problem

# Picking Numbers

Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to `1`.

##### **Example**

`a = [1,1,2,2,4,4,5,5,5]`

There are two subarrays meeting the criterion: `[1,1,2,2]` and `[4,4,5,5,5]` . The maximum length subarray has `5` elements.

**Input Format**

The first line contains a single integer`n` , the size of the array `a` .
The second line contains `n` space-separated integers, each an `a[i]`.

### Code :-

```c++
#include <bits/stdc++.h>

using namespace std;

int N;
int A[1000];

int main()
{
    cin>>N;
    for(int i=0; i<N; i++)
    {
        int a;
        cin>>a;
        A[a]++;
    }
    int ans=0;
    for(int i=1; i<1000; i++)
        ans=max(ans, A[i-1]+A[i]);
    cout<<ans<<endl;
    return 0;
}
```

#### **Input 1**

```` c++
6
4 6 5 3 3 1
````

#### **Output 1**

````c++
3
````

#### **Explanation 1**

````c++
We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference <= (i.e.,|4-3| = 1 and |3-3|=0), so we print the number of chosen integers,3, as our answer.
````

##### Similarly

#### **Input 2**

````c++
6
1 2 2 3 1 2
````

#### **Output 2**

````c++
5
````

