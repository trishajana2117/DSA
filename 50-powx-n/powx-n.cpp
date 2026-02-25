class Solution {
public:
    double myPow(double x, int n) {
        long long binForm = n;   // safer than long
        if(binForm < 0)
        {
            x = 1 / x;
            binForm = -binForm;
        }

        double ans = 1;

        while(binForm > 0)
        {
            if(binForm % 2 == 1)
            {
                ans *= x;
            }

            x *= x;           // always square
            binForm /= 2;     // always divide
        }

        return ans;
    }
};
