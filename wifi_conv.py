import csv, sys

conv_csv = []
with open(sys.argv[1], newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for line in spamreader:
        header = "WIFI:"
        passwd = ""
        if line[-1] == "UNKNOWN":
            continue
        if line[-1] == "OPEN":
            header += " "
        if line[-1].__contains__("WPA"):
            header += "T:WPA;"
            passwd = "P:" + line[1] + ";"
        body = "S:" + line[0] + ";"
        conv_csv.append(header+body+passwd+";")

print(conv_csv)
        