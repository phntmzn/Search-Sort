int jumpSearch(int arr[], int n, int target) {
    int step = sqrt(n);
    int prev = 0;
    while (arr[min(step, n)-1] < target) {
        prev = step;
        step += sqrt(n);
        if (prev >= n) return -1;
    }
    for (int i = prev; i < min(step, n); ++i)
        if (arr[i] == target)
            return i;
    return -1;
}
