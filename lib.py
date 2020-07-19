def draw_final_price(params):
  initial_price = params['S0']

  drift_term = (params['r'] - params['y'] - (params['sigma'] ** 2 / 2)) * params['T']
  vol_term = params['sigma'] * np.sqrt(params['T']) * np.random.normal()

  final_price = initial_price * np.exp(drift_term + vol_term)

  return final_price
