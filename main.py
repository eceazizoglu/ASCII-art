import random
import file_methods

# Run to see the amazing ASCII Art of Nature

big_little_dipper = file_methods.read("big_little_dipper.txt")
mountain = file_methods.read("mountain.txt")
northern_lights = file_methods.read("northern_lights.txt")
snowflakes = file_methods.read("snowflakes.txt")
sun = file_methods.read("sun.txt")
sunset = file_methods.read("sunset.txt")

choice = random.randint(1,6)
# can choose from inputs also.

if choice == 1:
  print(big_little_dipper)
elif choice == 2:
  print(mountain)
elif choice == 3:
  print(northern_lights)
elif choice == 4:
  print(snowflakes)
elif choice == 5:
  print(sun)
else:
  print(sunset)
