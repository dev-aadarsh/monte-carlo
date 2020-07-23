def draw_final_price(params):
  initial_price = params['S0']

  drift_term = (params['r'] - params['y'] - (params['sigma'] ** 2 / 2)) * params['T']
  vol_term = params['sigma'] * np.sqrt(params['T']) * np.random.normal()

  final_price = initial_price * np.exp(drift_term + vol_term)

  return final_price

def draw_paths(m, n, S0, T, r, y, sigma):
  paths = np.zeros((n, m + 1))
  paths[:,0] = S0

  for i in range(1, m + 1):
    z_arr = np.random.normal(size=n)
    delta_t = T

    drift_term = (r - y - (sigma ** 2 / 2)) * delta_t
    vol_term_arr = sigma * np.sqrt(delta_t) * z_arr
    exp_multiplier_arr = np.exp(drift_term + vol_term_arr)

    paths[:, i] = paths[:, i - 1] * exp_multiplier_arr
  
  return paths
