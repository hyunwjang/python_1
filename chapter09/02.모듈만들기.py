import pay_module


print(pay_module.vesion)


pay_module.printAuthor()


pay_info = pay_module.pay('a102030', 13000, '2021-06-03')
print(pay_info.get_pay_info())

print(pay_module.__name__)