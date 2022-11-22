import os


def ip_to_int(ip):
    """
    :type ip: str
    :rtype: int
    """
    int_ = 0
    for i in ip.split('.'):
        int_ = int_ << 8 | int(i)
    return int_


def int_to_ip(int_):
    """
    :type int_: int
    :rtype: str
    """
    ip = []
    for _ in range(4):
        ip.append(str(int_ & 255))
        int_ >>= 8

    return '.'.join(ip[::-1])


def exc(inf, ouf):
    file = open(inf, 'r')
    ofile = open(ouf, 'w')
    data = file.readlines()
    print("ipv4+ipv6: ", len(data))
    cnt = 0
    for d in data:
        if '.' in d:
            cnt += 1
            ip = d.split(" ")
            src = ip[0]
            dst = ip[1][:-1]
            src_int = ip_to_int(src)
            dst_int = ip_to_int(dst)
            ofile.write(str(src_int) + " ")
            ofile.write(str(dst_int) + "\n")
    print("ipv4: ", cnt)


if __name__ == '__main__':
    inf = r"E:\DeskTop\str_pkt"
    ouf = r"E:\DeskTop\train"
    # for txt in os.listdir(inf):
    #     exc(os.path.join(inf, txt), os.path.join(ouf, txt))
    f = open(r"E:\DeskTop\train\00.txt", 'r')
    da = f.readlines()[0].split(" ")
    print(da[0], int_to_ip(int(da[0])))