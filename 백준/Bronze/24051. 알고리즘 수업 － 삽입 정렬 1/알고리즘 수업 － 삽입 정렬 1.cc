#include<iostream>
#include<array>

using namespace std;

int checkInsertionsort(int a[], int n, int k) {
	int flag=0, i, j, item;
	for (i = 1; i < n; i++) {
		item = a[i];

		for (j = i - 1; j >= 0 && item < a[j]; j--) {
			a[j + 1] = a[j];
			flag++;
			if (flag == k) {
				//cout << a[j + 1] << endl;
				return a[j+1];
			}
		}


		if (j + 1 != i) {
			a[j + 1] = item;
			flag++;
			if (flag == k) {
				//cout << a[j + 1] << endl;
				return a[j+1];
			}

		}

	}

	return -1;
}

int main(void) {

	int ans, n, k;
	//int a[] = {4,5,1,3,2};
	int a[10001];
	int i, j = 0;

	cin >> n >> k;

	for (i = 0; i < n; i++) {
		cin >> a[i];
	}

	cout << checkInsertionsort(a, n, k) << endl;
	

}