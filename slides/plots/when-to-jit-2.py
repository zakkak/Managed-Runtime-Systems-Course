import sys
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sns.set(font_scale=1.25)
sns.set_style("white")
plt.figure(figsize=(9.6, 5), dpi=100)

t = [1, 2, 5, 10, 20, 50, 100]

x = np.linspace(1.01,20,1000)
y = x/(x-1)

for i in t:
    ax = sns.lineplot(x=x, y=y*i, palette="pastel", linewidth=3, label="τ="+str(i));
ax.set_ylabel("β");
ax.set_xlabel("ρ");
ax.set_yscale('log')
ax.set(ylim=(0.99,10000), xlim=(0,20))
ax.legend(ncol=4)
sns.despine()

# plt.plot(x, y*i, label="τ="+str(i))
plt.tight_layout();
plt.savefig("plots/when-to-jit-2.svg");