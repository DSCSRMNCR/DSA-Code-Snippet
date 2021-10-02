## Question

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

## Example:
~~~~~~~~~~~~
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:

ans = [ nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
ans = [1,2,1,1,2,1]
~~~~~~~~~~~~

## Code
~~~~~~~~~~~~
# include<bits/stdc++.h>
using namespace std;
# define ll long long int
#define ld long double
#define F first
#define S second
#define nl "\n"
#define mem(v, t) memset(v, t, sizeof(v))
#define all(v) v.begin(), v.end()
#define sz(v) (ll)(v.size())
#define srt(v) sort(all(v))
#define rsrt(v) sort(v.rbegin(), v.rend())
#define pb push_back
#define f(a) for (ll i = 0; i < a; i++)
#define rep(i, a, b) for (ll i = a; i < b; i++)
#define rrep(i, a, b) for (ll i = a; i > b; i--)
#define vll vector<ll>
#define pll pair<ll, ll>
#define vpll vector<pair<ll, ll>>
#define mp make_pair
#define PI 3.141592653589793238462643383279502884197169399375
#define INF (ll)(1e18 + 5)
#define fast ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL);
const int N=1e6+5;
const ll M=1000000007;
#define inf INT_MAX
#define ninf INT_MIN
#define tc ll t;  cin>>t; while(t--)
#define t0 __builtin_ctz

const ll mod=998244353;



void solve()
{
 ll n;  cin>>n;
 ll num[n];

 f(n)
 cin>>num[i];

 ll new_num[2*n];
 f(n)
 {
   new_num[i]=num[i];
   new_num[n+i]=num[i];
 }
 f(2*n)
 cout<<new_num[i]<<" ";

 cout<<nl;

}
int main()
{
 fast;
   //tc
   solve();
  
  return 0;
    
}
~~~~~~~~~~~~

## Contributed By
| Name | GitHub username | Institute |
| Dipti Agarwal | [Dipti821](https://github.com/Dipti821) | NIT Jamshedpur |
