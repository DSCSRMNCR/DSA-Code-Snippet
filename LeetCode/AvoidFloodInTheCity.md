#  Problem:  Avoid Flood in the city
##  Problem Statement
> Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the  `nth`  lake, the  `nth`  lake becomes full of water. If it rains ov a lake which is  **full of water**, there will be a  **flood**. Your goal is to avoid the flood in any lake.
> 
> Given an integer array  `rains`  where:
> 
> -   `rains[i] > 0`  means there will be rains over the  `rains[i]`  lake.
> -   `rains[i] == 0`  means there are no rains this day and you can choose  **one lake**  this day and  **dry it**.
> 
> Return  _an array  `ans`_  where:
> 
> -   `ans.length == rains.length`
> -   `ans[i] == -1`  if  `rains[i] > 0`.
> -   `ans[i]`  is the lake you choose to dry in the  `ith`  day if  `rains[i] == 0`.
> 
> If there are multiple valid answers return  **any**  of them. If it is impossible to avoid flood return  **an empty array**.
> 
> Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.
##  Code
```java
import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;
class avoidCityFlood {
    public static int[] avoidFlood(int[] rains) {
        if (rains == null || rains.length == 0) return rains;
        int[] res = new int[rains.length];
        Map<Integer, Integer> dates = new HashMap<>(); // track the day when a lake is filled
        TreeSet<Integer> availableDays = new TreeSet<>(); // track available days that can be used to empty lakes
        for (int i = 0; i < rains.length; i++) {
            if (rains[i] == 0) {
                availableDays.add(i);
                res[i] = 1; // placeholder, will be updated if we have to drain any lake on this day
            } 
            else {
                Integer lastDate = dates.get(rains[i]); // check whether the lake is filled
                if (lastDate != null) {
                    Integer day = availableDays.ceiling(lastDate); // check for the least day that we can drain the lake
                    // if the day is not available(either no '0's available or we don't have a '0' after the lake was filled last time
                    if (day == null) { 
                        return new int[]{};
                    } else {
                        res[day] = rains[i]; // update the day we should drain the lake
                        availableDays.remove(day);
                    }
                }
                res[i] = -1;
                dates.put(rains[i], i);
            }
        }
        return res;
    }
    public static void main(String[] args) {
        int[] rains = {1, 2, 0, 0, 2, 1}; //Example array
        int[] res = avoidFlood(rains);
        System.out.println("Output:");
        for (int re : res) {
            System.out.print(re+", ");
        }
    }
}
```
##  Output
```console
Output:
-1, -1, 2, 1, -1, -1, 
```
##  Contributed By
| Name | GitHub username | Institute |
|--|--|--|
| Abhinav Rajput | [AbhinavRajputEXE](https://github.com/AbhinavRajputEXE) | SRM, NCR campus, Modinagar |