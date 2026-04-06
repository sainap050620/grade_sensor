def grade_sensor(v):
  if v>80:
    print(f"{v}: Danger")
  elif v>50 and v<80:
    print(f"{v}: Medium")
  else:
    print(f"{v}: Low")
read = []
for r in range(5):
  read_inp = float(input(f"Enter reading number {r+1} to check"))
  read.append(read_inp)

# Call grade_sensor for each individual reading
print("\nSensor Readings Analysis:")
for reading_val in read:
  grade_sensor(reading_val)
