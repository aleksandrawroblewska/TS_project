from constans_given import initial_x, initial_y
from functions_algorithms import uchyb, change_to_z, change_to_h
# Można zmienić tylko wartości w ramkach
################################################################
#TODO: Pamietac o ograniczeniach:
# x +- 5,
# y -3, -20
goal_x = -2
goal_y = -13
################################################################

goal_h = change_to_h(goal_y)
goal_z = change_to_z(goal_x)

initial_z = change_to_z(initial_x)
initial_h = change_to_h(initial_y)
current_z = initial_z
current_h = initial_h
current_velocity_x = 0
current_velocity_y = 0
current_acceleration_x = 0
current_acceleration_y = 0



#initializing variables for results
time = [0]
results_z = [initial_z]
results_h = [initial_h]
results_x = []
results_y = []
velocity_x = [current_velocity_x]
velocity_y = [current_velocity_y]
velocity = [0]
acceleration_x = [0]
acceleration_y = [0]
acceleration = [0]
uchyb_x = [uchyb(initial_x, goal_x)]
uchyb_y = [uchyb(initial_y, goal_y)]
forces_1 = [0]
forces_2 = [0]
moments_1 = [0]
moments_2 = [0]
results_fi1 = [0]
results_fi2 = [0]