#include <bits/stdc++.h>
using namespace std;

#define PI 3.1415926535897932384626
#define ll long long
#define lli long long int
#define fo(i,a,n) for(int i=a;i<n;i++)
#define pr(i,arr) for(auto i:arr)

typedef vector<int> vi;
typedef vector<ll> vl;
typedef map<ll,ll> ml;
typedef map<int,int> mi;


void merge(vector<int> &array,int s,int e)
{
    int i =s;
    int m =(s+e)/2;
    int j = m+1;

    vector<int> temp;
    while(i<=m && j<=e)
    {
        if(array[i] < array[j])
        {
            temp.push_back(array[i]);
            i++;
        }
        else
        {
            temp.push_back(array[j]);
            j++;
        }
    }

    while(i<=m)
    {
        temp.push_back(array[i++]);
    }

    while(j<=e)
    {
        temp.push_back(array[j++]);
    }

    int k = 0;
    for(int idx=s;idx<=e;idx++)
    {
        array[idx] = temp[k++];
    }

    return ;
}

void mergeSort(vector<int> &arr,int s,int e)
{
    if(s>=e)
    {
        return;
    }

    int mid = (s+e)/2;
    mergeSort(arr,s,mid);
    mergeSort(arr,mid+1,e);
    return merge(arr,s,e);
}

void solve()
{
    int n;
    cin>>n;

    vector<int> v;
    for(int i=0;i<n;i++)
    {
        int a;
        cin>>a;
        v.push_back(a);
    }

    int s = 0;
    int e = n-1;
    mergeSort(v,s,e);

    for(auto it : v)
    {
        cout<<it<<" ";
    }

    cout<<endl;
    

}

int main() {

    solve();

    return 0;
}
