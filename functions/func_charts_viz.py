# func_charts_viz_01
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_boxplots(df: pd.DataFrame, column_names: list):
	"""
	Create box plots for specified columns in a DataFrame. 
	Function generates box plots for specified columns from the input DataFrame and visualizes them on a single chart. 

	Parameters:
	df (pd.DataFrame): The input DataFrame containing the data. 
	column_names (list): The list of column names to visualize.

	Returns:
	None
	"""
	# Adjust figure size based on the number of columns
	plt.figure(figsize=(10 * len(column_name), 6))

	# Set style to whitegrid for a cleaner look
	sns.set(style="whitegrid")

	# Create a new DataFrame with only the specified columns
	plot_df = df[column_names]

	# Melt the DataFrame to make it suitable for box plot
	plot_df = plot_df.melt(var_name='columns')

	# Create box plot with different colors for each box
	box_plot = sns.boxplot(x='columns', y='value', data=plot_df, palette=sns.color_palette("his", len(column_names)))

	# Set title, labels, and font sizes
	box_plot.set_title('Boxplots', fontsize=20)
	box_plot.set_xlabel('Columns', fontsize=15)
	box_plot.set_ylabel('Values', fontsize=15)

	# Increase the font size of the x and y tick labels
	box_plot.tick_params(axis='both', which='major', labelsize=13)

	# Check if all values in all columns are between 0 and 1
	if all(df[column].between(0, 1).all() for column in column_names):
		# Set y-axis as percentage
		box_plot.set_yticklabels(['{:.0f}%'.format(y * 100) for y in box_plot.get_yticks()])

	# Display the plot
	plt.show()
	

# func_charts_viz_02
def create_density_plots(df: pd.DataFrame, column_names: list):
	"""
	Create density plots for specified columns in a DataFrame.
	This function generates density plots (KDE plots) for the specified columns in the input DataFrame and visualizes them as overlapping line charts.

	Parameters:
	df (pd.DataFrame): The input DataFrame containing the data.
	column_names (list): The list of column names to visualize. 

	Returns:
	None
	"""
	# Adjust figure size based on the number of columns
	plt.figure(figsize=(10 * len(column_names), 6))

	# Set style to whitegrid for a cleaner look
	sns.set(style="whitegrid")

	# Create density plot for each column
	for column in column_names:
		sns.kdeplot(df[column], label=column, fill=True, linewidth=3, alpha=0.3)

	# Set title, labels, and font sizes
	plt.title('Density Plots', fontsize=15)
	plt.xlabel('Values', fontsize=15)
	plt.ylabel('Density', fontsize=15)

	# Increase the font size of the x and y tick labels
	plt.tick_params(axis='both', which='major', labelsize=15)

	# Add legend
	plt.legend(fontsize=15, title_fontsize=20, title='Legend', loc='upper right')

	# Display the plot
	plt.show()


# func_charts_viz_03
def create_histograms(df: pd.DataFrame, column_names: list):
	"""
	Create histograms for specific columns in a DataFrame. 
	Function generates histograms for the specific columns in the input DataFrame and visualizes them on a single chart. 

	Parameters:
	df (pd.DataFrame): The input DataFrame containing the data. 
	column_names (list): The list of column names to visualize. 

	Returns:
	None
	"""
	# Adjust figure size based on the number of columns
	plt.figure(figsize=(10 * len(column_names), 6))

	# Set style to whitegrid for a cleaner look
	sns.set(style="whitegrid")

	# Create a histogram for each column
	for column in column_names:
		sns.histplot(df[column], bins=100, label=column, linewidth=3, alpha=0.3)

	# Set title, labels, and font sizes
	plt.title('Histograms', fontsize=15)
	plt.xlabel('Values', fontsize=15)
	plt.ylabel('Frequency', fontsize=15)

	# Increase the font size of the x and y tick labels
	plt.tick_params(axis='both', which='major', labelsize=15)

	# Add legend
	plt.legend(fontsize=15, title_fontsize=20, title='Legend', loc='upper left')

	# Display the plot
	plt.show()


# func_charts_viz_04
import qrcode
from PIL import Image
# Generate image with QR code from any url pasted into "url" variable

def generate_qr_code(url: str, output_file: str = "qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    return Image.open(output_file)

url = "https://www.google.com/"
img = generate_qr_code(url)
img.show()


# func_charts_viz_05
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_box_charts(df, column_names):
	# Create a box plot for passed column names with percentage indication for (0,1)
    # Check if column names are provided as a list
    if not isinstance(column_names, list):
        raise ValueError("The column_names parameter should be a list of column names.")

    # Create a copy of the DataFrame to avoid modifying the original data
    df_copy = df.copy()

    # Initialize a flag for percentage conversion
    percentage_flags = []

    # Iterate over each column to check if values are between 0 and 1
    for column in column_names:
        if df_copy[column].between(0, 1).all():
            df_copy[column] = df_copy[column] * 100
            percentage_flags.append(True)
        else:
            percentage_flags.append(False)

    # Set the plot size and style
    plt.figure(figsize=(15, 8))
    sns.set_style("whitegrid")
    
    # Create a box plot for each column
    box_plot = sns.boxplot(data=df_copy[column_names], palette="Set3")

    # Customize the plot
    box_plot.set_title("Distribution of Selected Columns", fontsize=20)
    box_plot.set_ylabel("Values", fontsize=14)
    box_plot.set_xlabel("Columns", fontsize=14)
    box_plot.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Add percentage label to y-axis if applicable
    for idx, column in enumerate(column_names):
        if percentage_flags[idx]:
            box_plot.set_ylabel(f'{column} (Percentage)', fontsize=14)
            break  # Since we can only label the y-axis once, we break after the first match

    # Improve the background and grid style
    box_plot.set_facecolor('white')
    box_plot.xaxis.grid(True, which='major', linestyle='--', linewidth=0.5)
    box_plot.yaxis.grid(True, which='major', linestyle='--', linewidth=0.5)
    
    # Display the plot
    plt.show()

# Example usage:
df = pd.DataFrame({
    'example_column1': [0.1, 0.2, 0.5, 0.7, 0.9, 0.95, 0.6, 0.3, 0.8, 0.4],
    'example_column2': [0.15, 0.25, 0.55, 0.75, 0.85, 0.92, 0.65, 0.35, 0.82, 0.45],
    'example_column3': [10, 20, 50, 70, 90, 95, 60, 30, 80, 40]
})
plot_box_charts(df, ['example_column1', 'example_column2', 'example_column3'])


# func_charts_viz_06
