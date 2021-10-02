##Problem Link - (https://www.hackerrank.com/challenges/crush/problem)

#  Array Manipulation C++ Solution

Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

**Example**

n= 10

*queries* = [[1,5,3],[4,8,7],[6,9,1]]

![](C:\Users\anees\Pictures\Screenshots\Screenshot (41).png)

### **Explanation**

After the first update list will be `100 100 0 0 0`.
After the second update list will be `100 200 100 100 100`.
After the third update list will be `100 200 200 200 100`.
The required answer will be .

### Input format

The first line contains two space-separated integers `m` and `n` , the size of the array and the number of operations.
Each of the next lines contains three space-separated integers `x` , `y` and `k` , the left index, right index and summand.

### Code :-

```c++
#include <iostream>

using namespace std;
const int NMAX = 1e7+2;
long long a[NMAX];
int main()
{
    int n, m;
    cin >> n >> m;
    for(int i=1;i<=m;++i){
        int x, y, k;
        cin >> x >> y >> k;
        a[x] += k;
        a[y+1] -= k;
    }
    long long x = 0,sol=-(1LL<<60);
    for(int i=1;i<=n;++i){
        x += a[i];
        sol = max(sol,x);
    }
    cout<<sol<<"\n";
    return 0;
}
```

### Sample Input

> ```c++
> 5 3
> 1 2 100
> 2 5 100
> 3 4 100
> ```

### Sample Output

> 200



### Contributed By

|      Name       |              GitHub username              |         Institute         |
| :-------------: | :---------------------------------------: | :-----------------------: |
| Aneesh Tripathi | [Aneesh-07](https://github.com/Aneesh-07) | SRM,NCR campus, Modinagar |

