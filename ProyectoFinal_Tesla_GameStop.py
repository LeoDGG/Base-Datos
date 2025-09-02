#ProyectoFinal_Tesla_GameStop


import yfinance as yf

# Tesla
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="5y")
tesla_data.reset_index(inplace=True)

# GameStop
gamestop = yf.Ticker("GME")
gme_data = gamestop.history(period="5y")
gme_data.reset_index(inplace=True)
