void countingSort(int arr[], int n, int maxVal) {
    int count[maxVal+1];
    memset(count, 0, sizeof(count));
    for (int i = 0; i < n; ++i) count[arr[i]]++;
    for (int i = 0, j = 0; i <= maxVal; ++i)
        while (count[i]-- > 0) arr[j++] = i;
}
