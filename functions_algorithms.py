from cmath import sqrt

from matplotlib.pyplot import subplots, show, plot, xlabel, ylabel
from numpy import real


def diffrenciate(previous_value, current_value, step):
    result = (current_value - previous_value) / step
    return result


def integrate(previous_value, current_value, step):
    result = (current_value + previous_value) * step / 2
    return result


def change_to_x(z, a=8):
    return (z - a)


def change_to_y(h):
    return (-h)


def change_to_z(x, a=8):
    return (x + a)


def change_to_h(y):
    return (- y)


def uchyb(obecna_wartosc, zadana_wartosc):
    result = obecna_wartosc - zadana_wartosc
    return result


def pitagoras_przeciwprostokatna(wartosc_1, wartosc_2):
    return sqrt(wartosc_1 ** 2 + wartosc_2 ** 2)

def calculate_rope_difference(initial_value_1, initial_value_2, goal_value_1, goal_value_2):
    initial_l = pitagoras_przeciwprostokatna(initial_value_1, initial_value_2)
    final_l = pitagoras_przeciwprostokatna(goal_value_1, goal_value_2)
    difference_l = final_l - initial_l
    return difference_l

def checking_if_moments_in_scope(moment):
    if 0 > real(moment) or real(moment) > 20:
        print(f"Moment is out of scope equal to {moment}")

def plot_all_results(time, results_x, results_y, velocity_x, velocity_y, acceleration_x, acceleration_y, uchyb_x,
                     uchyb_y, results_fi1, results_fi2, moments_1, moments_2):
    fig, axs = subplots(3, 4)
    fig.suptitle('Wyniki przeprowadzonej symulacji')
    axs[0, 0].plot(time, results_x)
    axs[0, 0].set_xlabel('t [s]')
    axs[0, 0].set_ylabel('x')
    axs[1, 0].plot(time, results_y)
    axs[1, 0].set_xlabel('t [s]')
    axs[1, 0].set_ylabel('y')
    axs[0, 1].plot(time, velocity_x)
    axs[0, 1].set_xlabel('t [s]')
    axs[0, 1].set_ylabel('v_x')
    axs[1, 1].plot(time, velocity_y)
    axs[1, 1].set_xlabel('t [s]')
    axs[1, 1].set_ylabel('v_y')
    axs[0, 2].plot(time, acceleration_x)
    axs[0, 2].set_xlabel('t [s]')
    axs[0, 2].set_ylabel('a_x')
    axs[1, 2].plot(time, acceleration_y)
    axs[1, 2].set_xlabel('t [s]')
    axs[1, 2].set_ylabel('a_y')
    axs[0, 3].plot(time, uchyb_x)
    axs[0, 3].set_xlabel('t [s]')
    axs[0, 3].set_ylabel('uchyb_x')
    axs[1, 3].plot(time, uchyb_y)
    axs[1, 3].set_xlabel('t [s]')
    axs[1, 3].set_ylabel('uchyb_y')
    axs[2, 0].plot(time, results_fi1)
    axs[2, 0].set_xlabel('t [s]')
    axs[2, 0].set_ylabel('fi1')
    axs[2, 1].plot(time, results_fi2)
    axs[2, 1].set_xlabel('t [s]')
    axs[2, 1].set_ylabel('fi2')
    axs[2, 3].plot(time, moments_2)
    axs[2, 3].set_xlabel('t [s]')
    axs[2, 3].set_ylabel('M2')
    axs[2, 2].plot(time, moments_1)
    axs[2, 2].set_xlabel('t [s]')
    axs[2, 2].set_ylabel('M1')
    show()

def plot_path(results_x, results_y):
    plot(results_x, results_y)
    xlabel('x')
    ylabel('y')
    show()
