n = int(input())

dp = [[0 for i in range(2)] for j in range(n+1)]

dp[0][0]=1
dp[1][0]=1
dp[1][1]=2

for i in range(2,n+1):
    dp[i][0]=(dp[i-1][0]+dp[i-1][1])%9901
    dp[i][1]=(2*dp[i-1][0]+dp[i-1][1])%9901


print(sum(dp[n])%9901)