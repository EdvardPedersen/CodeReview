def asword(number):
    bigs = ["tjue", "tretti", "førti", "femti", "seksti", "søtti", "åtti", "nitti"]
    smalls = ["en", "to", "tre", "fire", "fem", "seks", "syv", "åtte", "ni", "ti", "elleve", "tolv", "tretten", "fjorten", "femten", "seksten", "søtten", "atten", "nitten"]
    if number < 20:
        return smalls[number - 1]
    nums = str(number)
    if int(nums[1]) > 0:
        return bigs[int(nums[0])-2] + smalls[int(nums[1])-1]
    return bigs[int(nums[0])-2]

for i in range(100):
    print(f"{i} {asword(i)}, {len(asword(i))}")

