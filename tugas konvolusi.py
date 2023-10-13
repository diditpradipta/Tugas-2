def convolution(signal, kernel):
    signal_len = len(signal)
    kernel_len = len(kernel)
    output_len = signal_len - kernel_len + 1
    output = [0] * output_len

    for i in range(output_len):
        for j in range(kernel_len):
            output[i] += signal[i + j] * kernel[j]

    return output

print("Naufal Kresnayana Pradipta")
print("5009211013")
# Example usage:
signal = [1, 2, 3, 4, 5, 6, 7]
kernel = [0.5, 0.5]

result = convolution(signal, kernel)
print(result)
