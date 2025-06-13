'''
Given two lists of length n, crew and position, map the space station crew to their position on board the international space station.

Each crew member crew[i] has job position[i] on board, where 0 <= i < n and len(crew) == len(position).

Hint: Introduction to dictionaries
'''
def space_crew(crew, position):
  return dict(zip(crew, position))


exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

print(space_crew(exp70_crew, exp70_positions))
print(space_crew(ax3_crew, ax3_positions))