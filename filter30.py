import os,sys

inf=open(sys.argv[1],"r")
ouf=open(sys.argv[1]+".m30.fq","w")

for line in inf:
	q=line.strip().split()
	if len(q)>9:
		s=q[9].count("a")+q[9].count("t")+q[9].count("c")+q[9].count("g")+q[9].count("n")
		if s>29 and "180bp_knob" in line:
			L=line.strip().split()
			ouf.write("@%s\n%s\n+\n%s\n"  % (L[0],L[9],L[10]) )

inf.close()
ouf.close()
