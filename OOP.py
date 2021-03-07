

class Employee:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@email.com'
		self.pay = pay

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		Employee.__init__(self, first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	def __init__(self, first, last, pay, Employees=None):
		Employee.__init__(self, first, last, pay)
		if Employees is None:
			self.Employees = []
		else:
			self.Employees = Employees

	def add_emp(self, emp) :
		if emp not in self.Employees:
			self.employees.append(emp)

	def remove_emp(self, emp) :
		if emp in self.Employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emmp in self.employees:
			print('-->', emp.fullname())


dev_1 = Developer('Minchul', 'Ahn', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)



# print(help(Developer))

