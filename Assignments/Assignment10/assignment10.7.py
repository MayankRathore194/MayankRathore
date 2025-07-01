import matplotlib.pyplot as plt

semesters = ["Sem 1", "Sem 2"]
marks = [88, 83]

plt.bar(semesters, marks, color=["blue", "green"])
plt.title("Semester Comparison")
plt.xlabel("Semester")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
