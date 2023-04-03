import matplotlib.pyplot as plt

f = open('reward.txt', 'r')
arr = [float(i.split('\n')[0]) for i in f.readlines()]
print(f'amount : {len(arr)}')
f.close()

moving_average = []
window_size = 100
for i in range(len(arr) - window_size + 1):
    window = arr[i:i+window_size]
    window_avg = sum(window) / window_size
    moving_average.append(window_avg)


plt.plot(arr, label='Rewards')
# plt.plot(arr[window_size-1:], label='Rewards') -> reward 100번째부터 표시

plt.plot(moving_average, label='Moving Average')
plt.legend()
plt.show()

