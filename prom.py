import math

# ==========================================
# ФИЗИЧЕСКИЕ ПОСТОЯННЫЕ
# ==========================================
C = 3e8              # Скорость света в вакууме, м/с
H = 6.626e-34        # Постоянная Планка, Дж*с
E = 1.6e-19          # Элементарный заряд (заряд электрона), Кл
M_E = 9.11e-31       # Масса электрона в состоянии покоя, кг

# =======================
# ВХОДНЫЕ ДАННЫЕ ВАРИАНТА 
# =======================
class VariantData:

    task1_u3 = 160.0       
    task2_lambda_min = 3.4 
    task3_p = 2.4          
    task4_lambda = 0.46    
    task5_u = 3.4          
    task8_i0 = 8.4         
    task8_r = 0.64         
    
    task9_alpha = 5.4      
    task9_n = 1.54         
    task10_i = 104.0       
    task10_x = 6.4         
    task10_d = 10.4        
    task11_phi = 104.0     
    task12_i0 = 8.4        
    task12_r = 0.64        
    
    task13_lambda = 0.8    
    task14_n = 6.0         
    task15_x = 6.0         
    task16_alpha = 4.74    
    task16_N = 3

# =============
# РЕШЕНИЯ ЗАДАЧ
# =============

def solve_task_1(u_z):
    print("\n--- Практическая работа №1 ---")
    u_m = math.sqrt(2) * 220
    fraction = 1 - (2 / math.pi) * math.asin(u_z / u_m)
    print("1. Амплитудное напряжение: U_m = sqrt(2) * 220")
    print("2. Доля периода: 2*Delta_t / T = 1 - (2/pi) * arcsin(U_z / U_m)")
    print(f"Ответ: Доля периода = {fraction:.4f}, частота вспышек n = 100 с^-1")

def solve_task_2(lambda_min_10_11):
    print("\n--- Практическая работа №2 ---")
    lambda_min_m = lambda_min_10_11 * 1e-11
    u_kv = ((H * C) / (E * lambda_min_m)) / 1000
    print("1. Формула для напряжения: U = (h*c) / (e * lambda_min)")
    print(f"Ответ: Напряжение на трубке U = {u_kv:.2f} кВ")

def solve_task_3(p_mw):
    print("\n--- Практическая работа №3 ---")
    p_watts = p_mw * 1e-3
    lambda_m = 630 * 1e-9
    n = (p_watts * 1.0 * lambda_m) / (H * C)
    print("1. Формула числа фотонов: N = (P * tau * lambda) / (h * c)")
    print(f"Ответ: Количество излучаемых фотонов за секунду N = {n:.2e}")

def solve_task_4(lambda_um):
    print("\n--- Практическая работа №4 ---")
    lambda_m = lambda_um * 1e-6
    lambda_max_m = 0.62 * 1e-6
    v = math.sqrt(((2 * H * C * (lambda_max_m - lambda_m))**2) / (M_E * lambda_m * lambda_max_m))
    print("1. Скорость: v = sqrt( (2*h*c*(lambda_max - lambda)) / (m*lambda*lambda_max) )")
    print(f"Ответ: Максимальная скорость фотоэлектронов v = {v:.2e} м/с")

def solve_task_5(u_volts):
    print("\n--- Практическая работа №5 ---")
    nu_0 = 6.0e14
    nu_max = nu_0 + (E * u_volts) / H
    print("1. Минимальная частота задержки: nu <= nu_0 + (e*U) / h")
    print(f"Ответ: Электроны задерживаются при частотах nu <= {nu_max:.2e} Гц")

def solve_task_6():
    print("\n--- Практическая работа №6 (Вывод формулы) ---")
    print("Закон сохранения энергии и импульса приводят к формуле эффекта Комптона:")
    print("Delta_lambda = (h / (m*c)) * (1 - cos(theta)) = (2*h / (m*c)) * sin^2(theta/2)")

def solve_task_7():
    print("\n--- Практическая работа №7 (Вывод энергии) ---")
    print("Минимальная кинетическая энергия протона выражается как:")
    print("W_k = (3 * Delta_m * c^2) / 2 = 3.3 МэВ")

def solve_task_8(i0, r):
    print("\n--- Практическая работа №8 ---")
    i_passed = i0 * (1 - r) / (1 + r)
    print("1. Полная интенсивность с учетом переотражений: I = I_0 * (1 - R) / (1 + R)")
    print(f"Ответ: Интенсивность прошедшего пучка I = {i_passed:.3f} Вт/м^2")

def solve_task_9(alpha_deg, n):
    print("\n--- Практическая работа №9 ---")
    alpha = math.radians(alpha_deg)
    beta = math.asin(n * math.sin(alpha))
    e2_e1 = (math.cos(beta - alpha) / math.cos(alpha)) * math.cos(beta)
    print("1. По закону преломления: sin(beta) = n * sin(alpha)")
    print("2. Отношение освещенностей: E2/E1 = (cos(beta - alpha) / cos(alpha)) * cos(beta)")
    print(f"Ответ: Освещенность изменится в {e2_e1:.3f} раз")

def solve_task_10(i_mw, x_mm, d_mm):
    print("\n--- Практическая работа №10 ---")
    h = d_mm / 2
    theta_1_deg = math.degrees(math.atan(h / x_mm))
    print(f"1. Половинный угол: theta_1 = arctg({h}/{x_mm}) = {theta_1_deg:.2f}°")
    
    i_vals = [0.99, 0.93, 0.82, 0.67, 0.5, 0.33, 0.18, 0.07, 0.008]
    num_int = 0
    for i in range(len(i_vals)):
        start_deg = i * 10
        end_deg = start_deg + 10
        if theta_1_deg <= start_deg:
            break
        actual_end = min(end_deg, theta_1_deg)
        term = i_vals[i] * (math.cos(math.radians(start_deg)) - math.cos(math.radians(actual_end)))
        num_int += term

    denom_int = 0.686 
    phi_c = i_mw * (num_int / denom_int)
    print(f"2. Интеграл числителя = {num_int:.4f}, интеграл знаменателя = {denom_int}")
    print(f"Ответ: Поток излучения на приемник Phi_c = {phi_c:.2f} мВт")

def solve_task_11(phi_sigma):
    print("\n--- Практическая работа №11 ---")
    i_ma = 8.6 * (phi_sigma / 100.0)
    print("1. Формула тока пропорциональна входному потоку.")
    print(f"2. Подстановка: I = 8.6 мА * ({phi_sigma} / 100)")
    print(f"Ответ: Ток фотодиода I = {i_ma:.2f} мА")

def solve_task_12(i0, r):
    print("\n--- Практическая работа №12 ---")
    i_passed = i0 * (1 - r) / (1 + r)
    print("1. Формула интенсивности: I = I_0 * (1 - R) / (1 + R)")
    print(f"Ответ: Интенсивность прошедшего пучка I = {i_passed:.3f} Вт/м^2")

def solve_task_13(lambda_um):
    print("\n--- Практическая работа №13 ---")
    lambda_m = lambda_um * 1e-6
    work_function_ev = 2.39 # Табличная работа выхода для лития, эВ
    a_work = work_function_ev * E 
    
    # Энергия падающего фотона
    e_photon = (H * C) / lambda_m
    
    if e_photon > a_work:
        ratio = 1 + (lambda_m / (200 * H)) * math.sqrt(2 * M_E * (e_photon - a_work))
        print("1. Формула отношения сил: F2/F1 = 1 + (lambda / 200h) * sqrt(2m * (hc/lambda - A))")
        print(f"2. Подставлена работа выхода лития A = {work_function_ev} эВ")
        print(f"Ответ: Сила изменится в {ratio:.4f} раз")
    else:
        print("Ответ: Длина волны слишком велика, фотоэффекта не будет (энергия фотона меньше работы выхода).")

def solve_task_14(n):
    print("\n--- Практическая работа №14 ---")
    a_coef = 1 + n
    b_coef = 2 * math.sqrt(n)
    print(f"1. Интенсивность I = I_A * [ (1+n) + 2*sqrt(n)*cos(k(r_B - r_A)) ]")
    print(f"2. Подставляем n = {n}: a_coef = 1+{n} = {a_coef}, b_coef = 2*sqrt({n}) = {b_coef:.2f}")
    print(f"Ответ: I = I_A[{a_coef} + {b_coef:.2f}cosk(r_B - r_A)]")

def solve_task_15(x_cm):
    print("\n--- Практическая работа №15 ---")
    eta = 8.53e23 # atom/cm^3
    n_inc = 10000
    n_out = 8950
    
    sigma_cm2 = (1 / (eta * x_cm)) * math.log(n_inc / n_out)
    sigma_barn = sigma_cm2 * 1e24
    
    r_cm = math.sqrt(sigma_cm2 / math.pi)
    r_fm = r_cm * 1e13 # Перевод из см в фемтометры (10^-15 м = 10^-13 см)
    
    print("1. Формула сечения: sigma = (1 / (eta * x)) * ln(N_inc / N)")
    print(f"   Подстановка: sigma = (1 / ({eta:.2e} * {x_cm})) * ln({n_inc} / {n_out})")
    print("2. Формула радиуса: R = sqrt(sigma / pi)")
    print(f"Ответ: Сечение sigma = {sigma_barn:.2f} барн, Радиус R = {r_fm:.2f} фм")

def solve_task_16(alpha_val, n_plates):
    print("\n--- Практическая работа №16 ---")
    # Перевод процентов в доли, если значение > 1
    a = alpha_val / 100.0 if alpha_val > 1 else alpha_val
    
    ans = (1 - a) / (1 + (n_plates - 1) * a)
    print("1. Формула относительной интенсивности: 1 - alpha_N = (1 - alpha) / (1 + (N - 1)*alpha)")
    print(f"   Подставляем alpha = {a:.4f} и N = {n_plates}")
    print(f"Ответ: Интенсивность 1 - alpha_N = {ans:.4f}")

if __name__ == "__main__":
    v = VariantData()
    solve_task_1(v.task1_u3)
    solve_task_2(v.task2_lambda_min)
    solve_task_3(v.task3_p)
    solve_task_4(v.task4_lambda)
    solve_task_5(v.task5_u)
    solve_task_6()
    solve_task_7()
    solve_task_8(v.task8_i0, v.task8_r)
    solve_task_9(v.task9_alpha, v.task9_n)
    solve_task_10(v.task10_i, v.task10_x, v.task10_d)
    solve_task_11(v.task11_phi)
    solve_task_12(v.task12_i0, v.task12_r)
    solve_task_13(v.task13_lambda)
    solve_task_14(v.task14_n)
    solve_task_15(v.task15_x)
    solve_task_16(v.task16_alpha, v.task16_N)
