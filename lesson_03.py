def read_file():
    f = open('requirements.txt', 'r')
    data = f.read()
    return data


read_file()


def fake_info():
    from faker import Faker
    fake = Faker()

    for _ in range(1, 101):
        print(_, fake.name(), fake.email())


fake_info()


def avg():
    r = open('hw.csv', 'r')
    h = []
    e = []
    w = []

    for i in r:
        if i != '\n':
            if '.' in i.split(',')[1]:
                h.append(float(i.split(',')[1]))
            if '.' in i.split(',')[2]:
                e.append(i.split(',')[2])

    for j in e:
        if '.' in j.split('\n')[0]:
            w.append(float(j.split('\n')[0]))

    h_sum = 0
    for k in h:
        h_sum += k

    w_sum = 0
    for g in w:
        w_sum += g

    w_avg = (w_sum / 25000) * 0.453

    h_avg = (h_sum / 25000) * 2.54
    return h_avg, w_avg


avg()

