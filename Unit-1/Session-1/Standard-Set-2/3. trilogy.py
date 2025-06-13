'''
Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.

Year	Movie Title
2005	"Batman Begins"
2008	"The Dark Knight"
2012	"The Dark Knight Rises"
If the given year does not match one of the years in the table above, print "Christopher Nolan did not release a Batman movie in <year>."
'''

def trilogy(year):
  '''
  Understand: Using an array, I can use tuples to answer this problem
  '''

  movies = [(2005, "Batman Begins"), (2008, "The Dark Knight"), (2012, "The Dark Knight Rises")]

  for movie in movies:
    if movie[0] == year:
      print(movie[1])
      return
      
  print(f"Christopher Nolan did not release a Batman movie in {year}")

year = 2008
trilogy(year)

year = 1998
trilogy(year)
