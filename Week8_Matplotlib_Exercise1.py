import matplotlib.pyplot as plt

data = {'begum': 25, 'asli': 30, 'sibil': 27, 'beyaz kedi': 20}
names = list(data.keys())
values = list(data.values())


fig, axs = plt.subplots()
axs.bar(names, values)
fig.suptitle('Categorical Plotting')

plt.show()

