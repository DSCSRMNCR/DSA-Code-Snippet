#  Problem: Longest Substring Without Repeating Characters
##  Problem Statement
>Given a string `s`, find the length of the **longest substring** without repeating characters.
>
> **Example :**
> 
> **Input:** s = "abcabcbb"
> 
> **Output:** 3
> 
> **Explanation:** The answer is "abc", with the length of 3.
##  Code
```java
import java.util.LinkedList;
class main {
    public static int lengthOfLongestSubstring(String s) {
        int maxlength = 0;
        char[] arr = s.toCharArray();
        LinkedList<Character> queue = new LinkedList<Character>();
        for (char c : arr) {
            if (queue.contains(c)) {
                while (queue.removeFirst() != c) {}
            }
            queue.add(c);
            maxlength = Math.max(queue.size(), maxlength);
        }
        return maxlength;
    }

    public static void main(String[] args) {
        String s = "abcabcbb";
        System.out.println("Input string: "+s);
        System.out.print("Output: ");
        int ans = lengthOfLongestSubstring(s);
        System.out.println(ans);
    }
}
```
##  Output
```console
Input string: abcabcbb
Output: 3
```
##  Contributed By
| Name | GitHub username | Institute |
|--|--|--|
| Abhinav Rajput | [AbhinavRajputEXE](https://github.com/AbhinavRajputEXE) | SRM, NCR campus, Modinagar |