from build_index import Index

obj = Index('db')
obj.print_index()
obj.update_index("hello.txt", {'hello': 1.53, 'why': 2.53})
obj.update_index("hello2.txt", {'hello': 1.23, 'why': 2.13})
obj.update_index("hello3.txt", {'hello': 1.23, 'why': 2.13})
obj.print_index()
# print(obj.get_result('why', 2))
# print(obj.get_result('why', 0))

print(obj.get_compound_result(['why', 'hello']))