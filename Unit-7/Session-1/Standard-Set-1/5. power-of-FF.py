def power_of_four(n):

  def power(base, exponent):
    if exponent == 0:
      return 1
    
    return base * power(base, exponent - 1)
  
  return power(n, 4)
  
print(power_of_four(2))
print(power_of_four(-2))