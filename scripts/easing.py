import matplotlib.pyplot as plt

def EaseInQuadratic(t):
    return t * t

def EaseOutQuadratic(t):
    t = (1.0 - t)
    return 1.0 - t * t

def EaseInOutQuadratic(t):
    if t <= 0.5:
        t *= 2.0
        return t * t * 0.5
    else:
        t = (1.0 - t) * 2.0
        return 1.0 - t * t * 0.5

def EaseInCubic(t):
    return t * t * t

def EaseOutCubic(t):
    t = (1.0 - t)
    return 1.0 - t * t * t 

def EaseInOutCubic(t):
    if t <= 0.5:
        t *= 2.0
        return t * t * t * 0.5
    else:
        t = (1.0 - t) * 2.0
        return 1.0 - t * t * t * 0.5

def EaseInQuartic(t):
    return t * t * t * t

def EaseOutQuartic(t):
    t = (1.0 - t)
    return 1.0 - t * t * t * t 

def EaseInOutQuartic(t):
    if t <= 0.5:
        t *= 2.0
        return t * t * t * t * 0.5
    else:
        t = (1.0 - t) * 2.0
        return 1.0 - t * t * t * t * 0.5

def EaseInQuintic(t):
    return t * t * t * t * t

def EaseOutQuintic(t):
    t = (1.0 - t)
    return 1.0 - t * t * t * t * t

def EaseInOutQuintic(t):
    if t <= 0.5:
        t *= 2.0
        return t * t * t * t * t * 0.5
    else:
        t = (1.0 - t) * 2.0
        return 1.0 - t * t * t * t * t * 0.5


def EaseInBack(t):
    c = 1.8
    return (c+1) * t * t * t - c * t * t

def EaseOutBack(t):
    t = (1.0 - t)
    c = 1.8
    return 1.0 - ((c+1) * t * t * t - c * t * t)

def EaseInOutBack(t):
    c = 1.8
    if t <= 0.5:
        t *= 2.0
        return ((c+1) * t * t * t - c * t * t) * 0.5
    else:
        t = (1.0 - t) * 2.0
        return (1.0 - ((c+1) * t * t * t - c * t * t)) * 0.5

def EaseOutBounce(t):
    if t < 4.0 / 11.0:
        t = t / 4.0 * 11.0
        return t * t
    elif t < 8.0 / 11.0:
        t = t - (4.0 / 11.0) - (2.0 / 11.0)
        return 1.0 + (t * t - (2.0 / 11.0) * (2.0 / 11.0)) * 8.0
    elif t < 10.0 / 11.0:
        t = t - (8.0 / 11.0) - (1.0 / 11.0)
        return 1.0 + (t * t - (1.0 / 11.0) * (1.0 / 11.0)) * 8.0
    else:
        t = t - (10.0 / 11.0) - (0.5 / 11.0)
        return 1.0 + (t * t - (0.5 / 11.0) * (0.5 / 11.0)) * 8.0

def EaseInBounce(t):
    return 1.0 - EaseOutBounce(1.0 - t)

def EaseInOutBounce(t):
    if t <= 0.5:
        t *= 2.0
        return EaseInBounce(t) * 0.5
    else:
        t = (t - 0.5) * 2.0
        return EaseOutBounce(t) * 0.5 + 0.5
easings = {}

easings['EaseInQuadratic'] = EaseInQuadratic
easings['EaseOutQuadratic'] = EaseOutQuadratic
easings['EaseInOutQuadratic'] = EaseInOutQuadratic

easings['EaseInCubic'] = EaseInCubic
easings['EaseOutCubic'] = EaseOutCubic
easings['EaseInOutCubic'] = EaseInOutCubic

easings['EaseInQuartic'] = EaseInQuartic
easings['EaseOutQuartic'] = EaseOutQuartic
easings['EaseInOutQuartic'] = EaseInOutQuartic

easings['EaseInQuintic'] = EaseInQuintic
easings['EaseOutQuintic'] = EaseOutQuintic
easings['EaseInOutQuintic'] = EaseInOutQuintic

easings['EaseInBack'] = EaseInBack
easings['EaseOutBack'] = EaseOutBack
easings['EaseInOutBack'] = EaseInOutBack

easings['EaseInBounce'] = EaseInBounce
easings['EaseOutBounce'] = EaseOutBounce
easings['EaseInOutBounce'] = EaseInOutBounce

for es_key, es_value in easings.items():
    xs = []
    ys = []
    for t in range(200):
        t /= 200.0
        xs.append(t)
        ys.append(es_value(t))

    plt.clf()
    plt.title(es_key)
    plt.plot(xs, ys)
    plt.savefig(es_key + '.png')

