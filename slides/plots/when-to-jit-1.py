import sys
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sns.set(font_scale=1.25)
sns.set_style("white")
plt.figure(figsize=(4.5, 4), dpi=100)

data = pd.DataFrame(np.array([[0, 0], [1, 2.5], [2, 3], [3, 3.5], [4, 4], [5, 4.5]]))
data.columns = ['A', 'B']
ax = sns.lineplot(data=data, palette="pastel", legend=False, linewidth=4, markers=["o", "v"], markersize=15);
ax.set_ylabel("Time");
ax.set_xlabel("Number of Executions");
ax.set(ylim=(0,5.5), xlim=(0,5.5))
sns.despine()
plt.tight_layout();
plt.savefig("plots/when-to-jit-1.svg");