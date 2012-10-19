# !/bin/python
from __future__ import division
import sys
import random

"""
The script is rewritten JavaScript as Python.
====================================================
<script type="text/javascript">
<!--
function pi(){
	n=document.forms[0].elements[0].value;
	p=0;
	for(i=0;i<=n;i++){
		x=Math.random();
		y=Math.random();
		if(x*x+y*y<=1) p++;
	}
	document.forms[0].elements[1].value=p/n*4;
}
//-->
</script>
"""


def getPI(n):
	p = 0
	for i in range(n+1):
		x = random.uniform(0,1)
		y = random.uniform(0,1)
		if (x*x + y*y <=1):
			p += 1
	return p / n * 4
		



if __name__ == "__main__":
	if (len(sys.argv[1:]) != 1):
		print "enter variable n please"
		sys.exit(0)

	# "start.."
	try:
		n = int(sys.argv[1])
		print getPI(n)
	except:
		print "enter variable n must be number"
	# print "Done!"
