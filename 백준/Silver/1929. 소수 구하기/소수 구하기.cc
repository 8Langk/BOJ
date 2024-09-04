#include<iostream>
#include<cmath>

using namespace std;

int main(void) {
	int n, m;
	int i = 0;
	int prime[1000001];

	cin >> n >> m;

	for (int i = 2; i <= m; i++) {
		prime[i] = i;
	}

	for (int i = 2; i <= m; i++) {
		if (prime[i] == 0) continue;
		for (int j = 2 * i; j <= m; j += i) {
			prime[j] = 0;

		}
	}

	for (int i = n; i <= m; i++) {
		if(prime[i]!=0)
			cout << i <<'\n';
	}




	return 0;
}