def FindSubarrayOfLengthKWithMaxPeak(arr, k):
    peaks = [0]*len(arr)

    # Mark the peaks
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            peaks[i] = 1

    # Prefix sum peaks
    for i in range(1, len(peaks)):
        peaks[i] += peaks[i-1]

    # Here -1 and +1 is because we should not consider the border elements for max_peaks
    max_peaks = peaks[k-1-1] - peaks[0+1]
    left = 0
    right = k-1

    # move window over peaks and keep result
    for i in range(k, len(peaks)):
        curr_peaks = peaks[i-1] - peaks[i-k+1]
        if curr_peaks > max_peaks:
            max_peaks = curr_peaks
            left = i-k+1
            right = i

    return (max_peaks, left+1, right+1)


print(FindSubarrayOfLengthKWithMaxPeak([3, 1, 4, 1, 5, 9, 2, 6], 7))
print(FindSubarrayOfLengthKWithMaxPeak([3, 2, 3, 2, 1], 3))