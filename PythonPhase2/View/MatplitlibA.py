import matplotlib.pyplot as plt
plt.xlabel('x',loc='right')
plt.ylabel('y',loc='center')
plt.title('Matplotlib')
plt.grid(True)
plt.xticks(rotation=90)

plt.plot([1,9,1,99],marker='D',linestyle='-',color='r',linewidth=3,ms=10.9,mfc='r',mec='k')
plt.show()
