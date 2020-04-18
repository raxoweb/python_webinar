import dategen

value = "i want report for july "
out = dategen.find_dates(value)
for v in out:
	print(type(v))
