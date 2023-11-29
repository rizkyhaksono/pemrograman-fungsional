from matplotlib import pyplot as plt
from numpy.random import normal
from numpy import mean, std
from scipy.stats import norm


sample = normal(loc=50, scale=5, size=1000)
plt.hist(sample, bins=10)
plt.show()

# percobaan 1
# plt.figure(figsize=(5,4))
# plt.hist(sample, bins=10, density=True)
# plt.show()

# percobaan 2
sample_mean = mean(sample)
sample_std = std(sample)
print("Mean=%.3f \nStandard Deviation=%.3f" % (sample_mean, sample_std))

# percobaan 3
dist = norm(sample_mean, sample_std)
dist

# percobaan 4
values = [value for value in range(30, 70)]
probabilitas = [dist.pdf(value) for value in values]
probabilitas

plt.hist(sample, bins=10, density=True)
plt.plot(values, probabilitas)
plt.show()
