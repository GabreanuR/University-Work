#include <iostream>
using namespace std;

void reverseArray(int arr[], const int size) {
    for (int i = 0; i < size / 2; ++i)
        swap(arr[i], arr[size - 1 - i]);
}

int sumArray(const int arr[], const int size) {
    int sum = 0;
    for (int i = 0; i < size; ++i)
        sum += arr[i];
    return sum;
}

double averageArray(int arr[], const int size) {
    return static_cast<double>(sumArray(arr, size)) / size;
}

int findMax(int arr[], const int size) {
    int maxVal = arr[0];
    for (int i = 1; i < size; ++i)
        maxVal = max(maxVal, arr[i]);
    return maxVal;
}

int main() {
    int arr[] = {10, 5, 8, 3, 12};
    constexpr int size = 5;

    cout << "Sum = " << sumArray(arr, size) << '\n';
    cout << "Average = " << averageArray(arr, size) << '\n';
    cout << "Max = " << findMax(arr, size) << '\n';

    reverseArray(arr, size);
    cout << "Reversed array: ";
    for (const int i : arr)
        cout << i << ' ';
    cout << '\n';

    return 0;
}
