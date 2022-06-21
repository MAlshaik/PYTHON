# Matplotlib is a graphical interface that makes plots for you
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y= x ** 2
print(x)
print(y)

#FUNCTIONAL METHOD TO PLOT USING MAT
plt.plot(x,y)
#plt.show() #prints plot
plt.xlabel('X label')
plt.ylabel('Y Label')
plt.title('Title')


plt.subplot(1,2,1)
plt.plot(x,y,'r')
#plt.show()

plt.subplot(1,2,2)
plt.plot(y,x,'b')
#plt.show()

#OBJECT ORIANTED METHOD
fig = plt.figure() #makes blank canvas(figure)
axes = fig.add_axes([0.1,0.1,0.8,0.8]) #makes axis
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3]) #[left, bottem, width, height]

axes1.plot(x,y)
axes2.plot(y,x)
plt.show()

fig,axes = plt.subplots(nrows=1, ncols=2) #makes plots based on the amount of rows and col
axes[0].plot(x,y) #plots on each individual axes created above ^^
axes[1].plot(y,x)
plt.show()

#FIGURE SIZE AND DPI
fig,axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2)) #figsize sets the dimentions of the figure by inch
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.show()

fig.savefig('my_graph.png', dpi=200)

fig = plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label='x Squared')
ax.plot(x,x**3,label='x cubed')

ax.legend(loc=0) # created a legend (label) that labels what each lines represents in the graph

plt.show()

#PLOT APPEARANCE
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color = '#FF8C00', linewidth = 3, linestyle= '--', marker = 'o', markersize = 10,
        markerfacecolor = 'black', markeredgewidth = 2, markeredgecolor = 'blue') #color is color of line, linewidth is thickness of line, alpha is transparancy, linestyle is style of line
ax.set_xlim([0,1]) #sets x limit (zooms in on area you want)
ax.set_ylim([0,2])#sets y limit (zooms in on area you want)
plt.show()



