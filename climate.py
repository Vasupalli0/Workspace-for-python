import pandas as pd
from tkinter import *
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 🪟 Setup main window
Window = Tk()
Window.title("ClimateScope 🌡️")
Window.geometry("500x500")
Window.configure(bg="#f0f4f8")

climate_data = None  # Dataset placeholder

# 📁 Load dataset and process 'Year' column
def load_dataset():
    global climate_data
    try:
        file_path = "GlobalLandTemperaturesByCountry.csv"  # 🔄 Replace with your actual path
        climate_data = pd.read_csv(file_path)

        # Extract year from 'dt' column
        climate_data['Year'] = pd.to_datetime(climate_data['dt']).dt.year

        # Drop rows with missing temperature
        climate_data = climate_data.dropna(subset=['AverageTemperature'])
        status_label.config(text="✅ Dataset loaded successfully!", fg="green")

    except Exception as e:
        status_label.config(text=f"⚠️ Error loading dataset: {str(e)}", fg="red")

# 🔮 Forecast temperature for a given year
def forecast():
    if climate_data is None:
        status_label.config(text="⚠️ Load the dataset first.", fg="red")
        return
    try:
        year = int(year_entry.get().strip())
        X = climate_data[['Year']]
        y = climate_data['AverageTemperature']

        model = LinearRegression()
        model.fit(X, y)

        prediction = model.predict([[year]])
        status_label.config(text=f"📅 {year} → Predicted Temp: {prediction[0]:.2f} °C", fg="black")

    except ValueError:
        status_label.config(text="⚠️ Please enter a valid year.", fg="red")

# 📈 Show a scatter plot of temperature trends
def show_plot():
    if climate_data is None:
        status_label.config(text="⚠️ Load dataset first to view plot.", fg="red")
        return

    plt.style.use('ggplot')
    plt.figure(figsize=(8, 5))
    plt.scatter(climate_data['Year'], climate_data['AverageTemperature'], color='dodgerblue', alpha=0.6)
    plt.title("Global Temperature Trend")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 🧱 GUI Elements
title_label = Label(Window, text="🌡️ ClimateScope Forecast Tool", font=("Segoe UI", 14, "bold"), bg="#f0f4f8")
title_label.pack(pady=10)

load_button = Button(Window, text="📁 Load Dataset", command=load_dataset, font=("Segoe UI", 10, "bold"), bg="#007acc", fg="white", relief=FLAT)
load_button.pack(pady=10)

year_label = Label(Window, text="Enter Year:", font=("Segoe UI", 12), bg="#f0f4f8")
year_label.pack(pady=5)

year_entry = Entry(Window, font=("Segoe UI", 12), justify="center")
year_entry.pack(pady=5)
year_entry.insert(0, "e.g. 2025")
year_entry.bind("<FocusIn>", lambda e: year_entry.delete(0, END))

forecast_button = Button(Window, text="📊 Forecast Temperature", command=forecast, font=("Segoe UI", 10, "bold"), bg="#28a745", fg="white", relief=FLAT)
forecast_button.pack(pady=10)

plot_button = Button(Window, text="📉 Show Climate Plot", command=show_plot, font=("Segoe UI", 10, "bold"), bg="#6f42c1", fg="white", relief=FLAT)
plot_button.pack(pady=10)

status_label = Label(Window, text="Dataset not loaded yet.", font=("Segoe UI", 11), wraplength=450, justify="center", bg="#f0f4f8", fg="black")
status_label.pack(pady=20)

# ▶️ Launch the app
Window.mainloop()











