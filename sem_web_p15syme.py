import csv

with open('schedule.csv', 'r', newline='') as ifp, open('lab2output.csv', 'w', newline='')as ofp:
	reader = csv.reader(ifp)
	writer = csv.writer(ofp)
	for row in reader:
		s = "b:" + row[0]
		p = row[1]
		
		if row[1] == "Ημέρα" or row[1] == "Ώρα":
			o = "l:" + row[2]
		else:
			o = "u:" + row[2]

		#print(s, p, o)

		writer.writerow([s, p, o])

with open('lab1output.csv', 'r', newline='') as ifp, open('lab2output.csv', 'w', newline='')as ofp:
	reader = csv.reader(ifp)
	writer = csv.writer(ofp)
	for row in reader:
		s = "b:" + row[0]
		p = row[1]
		
		if row[1] == "Ημέρα" or row[1] == "Ώρα":
			o = "l:" + row[2]
		else:
			o = "u:" + row[2]

		#print(s, p, o)

		writer.writerow([s, p, o])

with open('lab2output.csv', 'r', newline='') as ifp, open('lab3output.csv', 'w', newline='')as ofp:
	reader = csv.reader(ifp)
	writer = csv.writer(ofp)
	for row in reader:
		s = row[0]
		p = "http://host/sw/p15syme/myvocab#" + row[1]
		o = row[2]
		
		if o.startswith('u:'):
			o = 'http://host/sw/p15syme/resource/'
			for i in row[2][2:]:
				if i == " ":
					o += "%20"
				else:
					o += i

		print(s, p, o)

		writer.writerow([s, p, o])

with open('lab3output.csv', 'r', newline='') as ifp , open('lab4output.csv', 'w', newline='')as ofp:
        reader = csv.reader(ifp)
        writer = csv.writer(ofp)

        for row in reader:
          s = row[0].replace("b", "_") + "\t"
          p = "<" + row[1] + ">" + "\t"
          if row[2].startswith('l:'):
            o = row[2].replace("l:", ' ')
                if int in o:
                  o.split("-")
                  o = "Starts at:" + o.split("-")[0] + "Ends at: " + o.split("-")[1] + " ." 
          elif row[2].startswith('http'):
            o = "<" + row[2] + ">" + " ." + "\n"
          print (s,p,o)

with open('lab4output.csv',  'r', newline='') as ifp, open('timetable_rdf.nt', 'w') as ofp:
        reader = csv.reader(ifp)

        for s, p, o in reader:
            s1 = f'_:b{s[2:]}'
            p1 = f'<{p}>'
            if o[:2] == 'l:':
                o1 = o[2:]
                if 'Ώρα' in p:
                    o1 += ':00'
                o1 = f'"{o1}"'
            else:
                o1 = f'<{o}>'
            ofp.write(' '.join([s1, p1, o1]) + ' .\n')