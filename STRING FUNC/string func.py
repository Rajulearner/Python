var="pyTHoN IS EASY"
res=var.capitalize()
print(res)
res=var.title()

print(res)
res=var.upper()
print(res)
res=var.lower()
print(res)
res=var.swapcase()
print(res)
res=len(var)
print(res)
res=max(var)
print(res)
res=min(var)
print(res)
res=type(var)
print(res)
var="raju"
res=var.ljust(20,'#',)
print(res)
res=var.rjust(20,'#')
print(res)
res=var.center(20,'#')
print(res)
var="##san#tan##jai##"
res=var.lstrip('#')
print(res)
res=var.rstrip('#')
print(res)
res=var.strip('#')
print(res)
res=var.replace('#','')
print(res)
var="san@gmail.com"
res=var.startswith('sam')
print(res)
res=var.endswith('.com')
print(res)

var='hi python is easy i like python python rocks'
res=var.count('')
print(res)
res=var.find('python',33,len(var))
print(res)
res=var.index('python',3,len(var))
print(res)
