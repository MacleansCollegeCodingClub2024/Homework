print("Input a number (which will be the distance travelled)")

def the_bus_goes_round_and_round():


  base_fare = 5.00
  cost_per_stop_wow = 2.50

  start = int(input("Where is your starting stop?: "))
  end = int(input("Where are you gonna get dropped off!?: "))

  traveled = abs(end - start)
  total = base_fare + (traveled * cost_per_stop_wow)
  return total
fare = the_bus_goes_round_and_round()
print("Total cost:", fare)
print("Can you even afford this...")
