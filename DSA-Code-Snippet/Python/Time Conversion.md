
## Problem Link - (https://www.hackerrank.com/challenges/time-conversion/problem)

# Time Conversion C++ Solution

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

**Example**

- s = '12:01:00 PM'
 Return 12:01:00.
 
- s = '12:01:00 AM'
Return '00:01:00'.


### Input format
A single string 8 that represents a time in 12-hour clock format (i.e.:hh:mm:ssAM or hh:mm:ssPM)

### Code :-

```c++
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    string s;
    string h;
    int hr;
    cin>>s;
    hr = ((s[0]-'0')*10)+(s[1]-'0');
    if(s[8]=='P'&&s[9]=='M'&& hr ==12) cout<<to_string(hr);
    else if(s[8]=='P'&&s[9]=='M') cout<<to_string(hr+12);
    else if(s[8]=='A'&&s[9]=='M'&&hr==12) cout<<"00";
    
    else cout<< s[0]<<s[1];
    
   
    for(int i =2;i<8;i++)
        cout<<s[i];
    cout<<endl;
    return 0;
}
```

### Sample Input

```
07:05:45PM
```
### Sample Output

```
19:05:45
```

### Contributed By

|      Name       |              GitHub username              |         Institute         |
| :-------------: | :---------------------------------------: | :-----------------------: |
| Abhishek Tyagi | [Abhishek Tyagi](https://github.com/abhishektyagi2912) | SRM,NCR campus, Modinagar |
