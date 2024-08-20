import matplotlib.pyplot as plt
import numpy as np

# Data
parties = ['Republicans', 'Democrats', 'Independents']
yeas = [42, 48, 3]
nays = [7, 0, 0]
pres = [0, 0, 0]
nv = [0, 0, 0]

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 6))

bar_width = 0.5
index = np.arange(len(parties))

p1 = ax.bar(index, yeas, bar_width, label='Yeas', color='#2ecc71')
p2 = ax.bar(index, nays, bar_width, bottom=yeas, label='Nays', color='#e74c3c')
p3 = ax.bar(index, pres, bar_width, bottom=np.array(yeas)+np.array(nays), label='Present', color='#f39c12')
p4 = ax.bar(index, nv, bar_width, bottom=np.array(yeas)+np.array(nays)+np.array(pres), label='Not Voting', color='#95a5a6')

# Customize the chart
ax.set_ylabel('Number of Votes')
ax.set_title('S.1234 - Clean Energy Innovation Act of 2024\nUS Congress Voting Results')
ax.set_xticks(index)
ax.set_xticklabels(parties)
ax.legend()

# Add value labels on the bars
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 0:
            ax.text(rect.get_x() + rect.get_width()/2., rect.get_y() + height/2.,
                    f'{height}', ha='center', va='center')

add_labels(p1)
add_labels(p2)
add_labels(p3)
add_labels(p4)

# Add total votes text
total_votes = sum(yeas) + sum(nays) + sum(pres) + sum(nv)
ax.text(0.5, 1.05, f'Total Votes: {total_votes}', transform=ax.transAxes, ha='center', fontweight='bold')

plt.tight_layout()
plt.show()
