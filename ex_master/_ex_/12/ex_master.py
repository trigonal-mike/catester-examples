import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Spacial dimensions x, y
x = np.linspace(0, 2 * np.pi, 100)
cos_x = np.cos(x)

# Time dimension t
n_frames = 48
t = np.linspace(0, 2 * np.pi, n_frames)
cos_t = np.cos(t)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
line1 = axes.plot([], [], label="$cos(x) cos(t)$")[0]
line2 = axes.plot([], [], label="$cos(x - t)$")[0]

axes.set(xlim=[min(x), max(x)], ylim=[-1, 1])
axes.legend(loc="upper left")


def update(frame_num):
    """for each frame, update the data stored on each artist."""

    line1.set_xdata(x)
    line1.set_ydata(cos_x * cos_t[frame_num])

    line2.set_xdata(x)
    line2.set_ydata(np.cos(x - t[frame_num]))

    return (line1, line2)


ani = animation.FuncAnimation(
    fig=fig, func=update, frames=n_frames, interval=16, blit=True
)
plt.show()

ani.save(filename="cos_animation_reference.gif", writer="pillow")


l1, l2 = update(12)

print(l1)
print(l2)
print(type(l1))
print(type(l2))
#$META title "Animation"
#$VARIABLETEST variables
#$TESTVAR x
#$TESTVAR t
#$TESTVAR cos_t

#$VARIABLETEST func
#$PROPERTY setUpCode ["l1, l2 = update(12)"]
#$TESTVAR l1
#$TESTVAR l2
