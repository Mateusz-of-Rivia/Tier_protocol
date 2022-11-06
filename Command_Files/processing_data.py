#!/usr/bin/python
# -*- coding: utf-8 -*-
with open('weather.txt') as weatherfile:
    lines = weatherfile.readlines()
weather = []
i = 0
for line in lines:
    if line.find("MX0000170042010") != -1:
        i += 1
        weather.append(line)
        if i == 15:
            break

id = "MX000017004"
rows = []
for row in weather:
    it = len(id)
    year = row[it:it + 4]
    month = row[it + 4:it + 4 + 2]
    element_type = row[it + 4 + 2:it + 4 + 2 + 4]
    days_1 = row[it + 4 + 2 + 4:].split()
    day_data = row[it + 4 + 2 + 4:]
    if len(days_1) > 31:
        days_1 = days_1[:31]
    to_return = []
    for el in days_1:
        if el == 'S-9999' or el == 'S' or el == '-9999':
            el = 'inf'
            to_return.append(el)
        else:
            to_return.append(el)
    rows.append([id, year, month, element_type] + to_return)

result = ["id           date       TMAX  TMIN  PRCP"]
day_in_month = [31,28,31,30,31]
month = 0
for days in day_in_month:
    month += 1
    for i in range(days):
        date = ""
        if i > 8:
            date = "2010-0" + str(month) + "-" + str(i +1)
        else:
            date = "2010-0" + str(month) + "-0" + str(i +1)

        result_row = [id, date, rows[month * 3 - 3][i+4], rows[month * 3 - 2][i+4], rows[month * 3 -1][i+4]]
        result.append(result_row)
for i in range(1, len(result)):
    result[i] = '  '.join(result[i])
result = "\n".join(result)

f = open("appendix_data.txt", "w")
f.write(result)
