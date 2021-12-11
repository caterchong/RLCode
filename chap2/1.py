import matplotlib.pyplot as plt
import random

step = 500

bandit = [random.random()*5 for x in range(10)]
print(bandit)

greedyRewardHistory = []

stat = [10]*len(bandit)
cnt = [0]*len(bandit)
for i in range(step):
    greedyIndex = stat.index(max(stat))
    reward = random.normalvariate(bandit[greedyIndex], 1)
    cnt[greedyIndex] += 1
    stat[greedyIndex] += (reward - stat[greedyIndex])/cnt[greedyIndex]
    greedyRewardHistory.append(reward)
print(cnt)


ep1RewardHistory = []
stat = [10]*len(bandit)
cnt = [0]*len(bandit)
for i in range(step):
    index = stat.index(max(stat))
    if random.random() < 0.1:
        index = random.randint(0, len(bandit) - 1)
    reward = random.normalvariate(bandit[index], 1)
    cnt[index] += 1
    stat[index] += (reward - stat[index])/cnt[index]
    ep1RewardHistory.append(reward)
print(cnt)

plt.plot(greedyRewardHistory, label="greedy")
plt.plot(ep1RewardHistory, label="epsilon")
plt.legend()
plt.show()
