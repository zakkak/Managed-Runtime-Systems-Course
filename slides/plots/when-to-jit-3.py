import sys
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sns.set(font_scale=1.25)
sns.set_style("white")
plt.figure(figsize=(9.6, 5), dpi=100)

x = np.linspace(0,1000000,10000)
y = x*5/(x+5*100)

ax = sns.lineplot(x=x, y=y, palette="pastel", linewidth=3, legend=False);
sns.lineplot(x=x, y=1, palette="pastel", linewidth=1, label="y=1");
sns.lineplot(x=x, y=5, palette="pastel", linewidth=1, label="y=ρ");
ax.plot([125,5], [125,0], label="x=125")
ax.legend()
for i in range(1,4):
    ax.lines[i].set_linestyle("--")
ax.set_ylabel("β");
ax.set_xlabel("ρ");
ax.set_yscale('log')
ax.set_xscale('log')
ax.set(ylim=(0.008,10), xlim=(1,1000000))
sns.despine()

# plt.plot(x, y*i, label="τ="+str(i))
plt.tight_layout();
plt.savefig("plots/when-to-jit-3.svg");