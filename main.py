from constans_given import r1, r2, simulation_time, dt, m, g
from functions_algorithms import pitagoras_przeciwprostokatna, change_to_x, change_to_y, diffrenciate, integrate, \
    uchyb, calculate_rope_difference, checking_if_moments_in_scope, plot_all_results, plot_path
from other_constans import time, velocity_x, velocity_y, velocity, acceleration, uchyb_x, uchyb_y, results_x, \
    results_y, results_h, results_z, initial_h, initial_z, goal_h, goal_z, acceleration_x, acceleration_y, current_z, \
    current_h, moments_1, moments_2, forces_1, forces_2, results_fi1, results_fi2

if __name__ == '__main__':

    #Calculating the rope differences
    difference_l1 = calculate_rope_difference(initial_h, initial_z, goal_h, goal_z)
    difference_l2 = calculate_rope_difference(initial_h, (16 - initial_z), goal_h, (16 - goal_z))

    #Calculating rotation angles
    fi1 = difference_l1/r1
    fi2 = difference_l2/r2

    #Calculating velocity of rotations
    velocity_rotation_1 = fi1/simulation_time
    velocity_rotation_2 = fi2/simulation_time

    #Changing it to velocities of respective ropes
    velocity_rope_1 = velocity_rotation_1 * r1
    velocity_rope_2 = velocity_rotation_2 * r2


    for i in range(1, 1000):
        #time
        time.append(dt*i)

        #velocity
        current_velocity_x = (goal_z - initial_z)/simulation_time
        current_velocity_y = (goal_h - initial_h)/simulation_time
        #ruch zmienny
        # current_velocity_x = velocity_rope_1 * \
        #                      current_z/pitagoras_przeciwprostokatna(current_h, current_z)
        # current_velocity_y = velocity_rope_2 * \
        #                      current_z / pitagoras_przeciwprostokatna(current_h, (16-current_z))
        velocity_x.append(current_velocity_x)
        velocity_y.append(current_velocity_y)
        velocity.append(pitagoras_przeciwprostokatna(current_velocity_y, current_velocity_x))

        #acceleration
        current_acceleration_x = diffrenciate(velocity_x[i-1], velocity_x[i], dt)
        current_acceleration_y = diffrenciate(velocity_y[i-1], velocity_y[i], dt)
        acceleration_x.append(current_acceleration_x)
        acceleration_y.append(current_acceleration_y)
        acceleration.append(pitagoras_przeciwprostokatna(current_acceleration_y, current_acceleration_x))

        #locations
        current_h = current_h + integrate(velocity_y[i-1], velocity_y[i], dt)
        results_h.append(current_h)
        current_z = current_z + integrate(velocity_x[i-1], velocity_x[i], dt)
        results_z.append(current_z)

        # force
        current_force_x = current_acceleration_x * m
        current_force_y = current_acceleration_y * m
        force_2 = m * g * pitagoras_przeciwprostokatna(current_h, (16 - initial_z)) * current_z / (16 * current_h)
        force_1 = force_2 * ((16 - current_z)/pitagoras_przeciwprostokatna(current_h, (16 - initial_z)))/\
                  (current_h/(pitagoras_przeciwprostokatna(current_h, current_z)))
        m1 = force_1 * r1
        m2 = force_2 * r2
        checking_if_moments_in_scope(m1)
        checking_if_moments_in_scope(m2)

        forces_1.append(force_1)
        forces_2.append(force_2)
        moments_1.append(m1)
        moments_2.append(m2)

        #uchyb
        uchyb_x.append(uchyb(results_z[i], goal_z))
        uchyb_y.append(uchyb(results_h[i], goal_h))

        #katy obrotu
        results_fi1.append(fi1*dt/simulation_time*i)
        results_fi2.append(fi2*dt/simulation_time*i)

    #TODO: zrobic to lepiej
    uchyb_y[0] = uchyb_y[1]

    #transformation back to x, y axes
    for zs in results_z:
        results_x.append(change_to_x(zs))
    for hs in results_h:
        results_y.append(change_to_y(hs))

    plot_path(results_x, results_y)

    plot_all_results(time, results_x, results_y, velocity_x, velocity_y, acceleration_x, acceleration_y, uchyb_x,
                     uchyb_y, results_fi1, results_fi2, moments_1, moments_2)

