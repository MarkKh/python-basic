texinput = float(input("tax employee A is : "))
employeeA, employeeB, employeeC = 5000, 10000, 20000
texsalaryA = (employeeA * (texinput/100))*12
texsalaryB = (employeeB * (texinput*2/100))*12
texsalaryC = (employeeC * (texinput*3/100))*12
summaries = texsalaryA + texsalaryB + texsalaryC

print("Employee A tax/year is :",texsalaryA)
print("Employee B tax/year is :",texsalaryB)
print("Employee C tax/year is :",texsalaryC)
print("Summaries all employee tax/year is :",round(summaries,2))
