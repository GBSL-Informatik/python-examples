from smartphone_connector import Connector, GyroMsg
import matplotlib.pyplot as plt
phone = Connector('https://io.gsbl.website', 'FooBar')
MAX_SAMPLES = 300

y = []
x = []
plt.show()


def on_gyro(data: GyroMsg):
    if len(x) > MAX_SAMPLES:
        x.pop(0)
        y.pop(0)

    x.append(data.time_stamp)
    y.append([data.alpha, data.beta, data.gamma])


def on_intervall():
    plt.clf()
    plt.plot(x, y)
    plt.pause(0.01)


phone.on_gyro = on_gyro
phone.subscribe(on_intervall, interval=0)
