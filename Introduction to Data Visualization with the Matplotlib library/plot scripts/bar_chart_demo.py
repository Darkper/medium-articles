from matplotlib import pyplot as plt

pairs_owned = [16, 9, 9, 6]
options = ["One", "Two", "Three", "Four+"]

# Plot the years of experience working with Python of 40 individuals in a bar chart
plt.bar(options, pairs_owned)

plt.title("Years of experience working with Python (n=40)")
plt.ylabel("Number of respondents")
plt.tight_layout()
plt.savefig("bar_chart_demo.png")
plt.show()
