#module is used for better organize our code

import converters_module
from converters_module import lbs_to_kg
from largest_number_using_function import find_max

print(converters_module.kg_to_lbs(70))
print(lbs_to_kg(60))

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)

