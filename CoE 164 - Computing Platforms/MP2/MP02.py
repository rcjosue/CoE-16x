import cmath


def get_e(samples):
    return samples[0::2]

def get_a(samples):
    return samples[1::4]

def get_b(samples):
    return samples[3::4]

def compute_twiddling_factor(N):
    twiddling_factor = []
    for i in range(N):
        twiddling_factor.append(cmath.exp((-2j*cmath.pi*i)/N))
    # print("TF:",twiddling_factor)
    return twiddling_factor

def dft(samples):
    if len(samples) == 2:
        return [samples[0]+samples[1], samples[0] - samples[1]]
    if len(samples) == 1:
        return samples
    a = get_a(samples)
    b = get_b(samples)
    e = get_e(samples)

    dft_a = dft(a)
    dft_b = dft(b)
    dft_e = dft(e)
    # print(dft(e))
    twiddling_factor = compute_twiddling_factor(len(samples))
    sum_odd = []
    diff_odd = []
    for i in range(len(dft_a)):
        sum_odd.append(twiddling_factor[i]*dft_a[i] + twiddling_factor[i*3]*dft_b[i])
        diff_odd.append(twiddling_factor[i]*dft_a[i] - twiddling_factor[i*3]*dft_b[i])
        # print("sum_odd: ",sum_odd,twiddling_factor[i],dft_a[i],twiddling_factor[i*3],dft_b[i])
    # print(sum_odd)
    # print(diff_odd)
    # print(dft_e)
    X0 = []
    X1 = []
    X2 = []
    X3 = []

    for i in range(len(sum_odd)):
        X0.append(dft_e[i] + sum_odd[i])
        X1.append(dft_e[i + len(samples)//4] - 1j*diff_odd[i])
        X2.append(dft_e[i] - sum_odd[i])
        X3.append(dft_e[i + len(samples)//4] + 1j*diff_odd[i])
        # print("X0 appended:",dft_e[i], sum_odd)
    return X0+X1+X2+X3


T = int(input())
while(T):
    # compute_twiddling_factor(1)
    line = list(map(int, input().split()))
    N_sample = line[0]
    sample_points = line[1:]
    # if (N_sample - 3) % 4 == 0:
    #     sample_points.append(0)
    # print(sample_points)

    result = 1;
    while(result < N_sample):
        result *= 2
    
    for i in range(result - N_sample):
        sample_points.append(0)

    print(sample_points)
    e = get_e(sample_points)
    a = get_a(sample_points)
    b = get_b(sample_points)
    result = dft(sample_points)
    for i in range(len(result)):
        result[i] = round(result[i].real, 6) + round(result[i].imag, 6)*1j
    print("Result:", result)
    T-=1