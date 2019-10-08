from src.services.object import Object

prefix = '/app/mech4u/src/tests/'
filenames = [
    'part1.stp',
    'part2.stp',
    'part3.stp',
    'part4.stp',
    'part5.stp',
]

for name in filenames:
    obj = Object(prefix + name)

    print(obj.get_all_info())
