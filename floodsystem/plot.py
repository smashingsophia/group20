import matplotlib.pyplot as plt
import numpy as np



def plot_water_levels(station, dates, levels):


# Plot
    plt.plot(dates, levels)
    plt.axhline(y = station.typical_range[0], color = 'r', linestyle = '-')
    plt.axhline(y = station.typical_range[1], color = 'r', linestyle = '-')

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

# Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
    
def plot_water_level_with_fit(station, dates, levels, p):
    
    
    
    p_coeff = np.polyfit(dates, levels, p)

# Convert coefficient into a polynomial that can be evaluated,
# e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

# Plot original data points
    plt.plot(dates, levels, '.')
    #plt.plot(dates, levels)
    plt.axhline(y = station.typical_range[0], color = 'r', linestyle = '-')
    plt.axhline(y = station.typical_range[1], color = 'r', linestyle = '-')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

# Plot polynomial fit at 30 points along interval
    x1 = np.linspace(dates[0], dates[-1], 30)
    plt.plot(x1, poly(x1))
    plt.tight_layout()  

    plt.show()
    