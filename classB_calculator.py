import argparse

cidrMap = {
    0: 4294967296,
    1: 2147483648,
    2: 1073741824,
    3: 536870912,
    4: 268435456,
    5: 134217728,
    6: 67108864,
    7: 33554433,
    8: 16777216,
    9: 8388608,
    10: 4194304,
    11: 2097152,
    12: 1048576,
    13: 524288,
    14: 262144,
    15: 131072,
    16: 65536,
    17: 32768,
    18: 16384,
    19: 8192,
    20: 4096,
    21: 2048,
    22: 1024,
    23: 512,
    24: 256,
    25: 128,
    26: 64,
    27: 32,
    28: 16,
    29: 8,
    30: 4,
    31: 2,
    32: 1
}

def buildParser():
    cliParse = argparse.ArgumentParser()
    cliParse.add_argument("-l", "--large", help="the larger subnet, that will be broken into smaller subnets")
    cliParse.add_argument("-s", "--small", help="the smaller CIDR (only cidr, not enture subnet), that is derived from the larger subnet")
    args = cliParse.parse_args()
    onlyVals = {k: v for k, v in vars(args).items() if v is not None}
    return onlyVals

def genSubnets(large, small):
    # MATH LOGIC:
    #   •to get total number of smaller subnets fit inside larger subnet
    #       •2 to the power of  (smaller subnet - larger subnet) = your answer
    #           •Example A:
    #               Larger subnet = /20
    #               Smaller subnet = /26
    #               Formula:  2 to the power of (26 - 20, which is 6)
    #                         2^6 = 64 subnets of size /26 fit inside a /20
    #           •Example B:
    #               Larger subnet = /16
    #               Smaller subnet = /24
    #               Formula:  2 to the power of (24 - 16, which is 8)
    #                         2^8 = 256 subnets of size /24 fit inside a /16
    #   •to get number of iterations to run to create all necessary smaller CIDR's
    #       •octets are 8 bits, and have a decimal range of 0-255 (256 total, counting starts at 0)
    #       •divide the number 256 against the number of IP's possible from the smaller CIDR
    #           •Example A - 192.168.32.0/19, break into smaller /26:
    #               -256 possible addresses
    #               -/26 CIDR has 64 addresses
    #               -256 / 64 = 4 (last octect has 4 entries, 0-63, 64-127, 128-191, 192-255)
    totalNumSmallSubnets = 2 ** (int(small.split("/")[-1]) - int(large.split("/")[-1]))
    numCIDRs = 256 / cidrMap[int(small.split("/")[-1])]
    iterationRange = int(totalNumSmallSubnets) / int(numCIDRs)
    smallRange = cidrMap[int(small.split("/")[-1])]
    subnet = large.split("/")[0]
    ipSplit = subnet.split(".")
    f = 0
    # f variable ensures first loop starts last octet of IP at 0, every iteration after will increment the 3rd octet of the IP subnet
    for x in range(int(iterationRange)):
        if f == 0:
            a = 0
            for y in range(int(numCIDRs)):
                if y == 0:
                    print(ipSplit[0] + "." + ipSplit[1] + "." + ipSplit[2] + "." + str(a) + "-" + small.split("/")[-1])
                else:
                    a += smallRange
                    print(ipSplit[0] + "." + ipSplit[1] + "." + ipSplit[2] + "." + str(a) + "-" + small.split("/")[-1])
            f += 1
        else:
            a = 0
            for y in range(int(numCIDRs)):
                incrementedNum = int(ipSplit[2]) + int(x)
                if y == 0:
                    print(ipSplit[0] + "." + ipSplit[1] + "." + str(incrementedNum) + "." + str(a) + "-" + small.split("/")[-1])
                else:
                    a += smallRange
                    print(ipSplit[0] + "." + ipSplit[1] + "." + str(incrementedNum) + "." + str(a) + "-" + small.split("/")[-1])

def main():
    parsedArgs = buildParser()
    genSubnets(parsedArgs["large"], parsedArgs["small"])

if __name__ == '__main__':
    main()
