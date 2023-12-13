import logging
from consolemenu import PromptUtils, Screen, ConsoleMenu
from consolemenu.items import FunctionItem
from consolemenu.validators.base import BaseValidator
import pandas as pd
import os
import matplotlib.pyplot as plt

from share.menu import Menu, menu_item
from share.config import Config
config = Config("data/lab8/config.json")

class PathValidator(BaseValidator):
    def validate(self, input_string: str) -> bool:
        return os.path.isfile(input_string)

class ColumnValidator(BaseValidator):
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        super().__init__()

    def validate(self, input_string: str) -> bool:
        return input_string in self.df.columns 

class Vizualizer(Menu):
    def __init__(self) -> None:
        super().__init__()

        # self.menu.append_item(FunctionItem("Show table", self.show_table))
        # self.menu.append_item(FunctionItem("Show extremes", self.show_extremes))
        # self.menu.append_item(FunctionItem("Show plot", self.show_plot))
        # self.menu.append_item(FunctionItem("Export", self.export))
        
        csv_path = config["csv_path"]
        
        self.csv: pd.DataFrame = pd.read_csv(csv_path)

    @menu_item("Export")
    def export(self):
        export_menu = ConsoleMenu("Export Visualization", "Select the type of plot to export:")
        export_menu.append_item(FunctionItem("Export Line Plot", self.export_line_plot))
        export_menu.append_item(FunctionItem("Export Bar Chart", self.export_bar_chart))
        export_menu.append_item(FunctionItem("Export Scatter Plot", self.export_scatter_plot))
        export_menu.append_item(FunctionItem("Export Histogram", self.export_histogram))
        export_menu.append_item(FunctionItem("Export Pie Chart", self.export_pie_chart))

        export_menu.show()

    def export_line_plot(self):
        pu = PromptUtils(Screen())
        x_column = ''
        while True:
            res = pu.input("Enter the column for the X axis: ", validators=[ColumnValidator(self.csv)])

            if res[1]:
                x_column = res[0]
                break
        
        y_column = ''
        while True:    
            res = pu.input("Enter the column for the Y axis: ", validators=[ColumnValidator(self.csv)])

            if res[1]:
                y_column = res[0]
                break

        plt.plot(self.csv[x_column], self.csv[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"Line Plot of {y_column} vs {x_column}")
        plt.savefig(config["save_path"] + '/line_plot.png')

    def export_bar_chart(self):
        category_column = input("Enter the category column: ")
        value_column = input("Enter the value column: ")

        self.csv.groupby(category_column)[value_column].sum().plot(kind='bar')
        plt.xlabel(category_column)
        plt.ylabel(value_column)
        plt.title(f"Bar Chart of {value_column} by {category_column}")
        plt.savefig(config["save_path"] + '/bar_plot.png')

    def export_scatter_plot(self):
        pu = PromptUtils(Screen())
        x_column = ''
        while True:
            res = pu.input("Enter the column for the X axis: ", validators=[ColumnValidator(self.csv)])

            if res[1]:
                x_column = res[0]
                break
        
        y_column = ''
        while True:    
            res = pu.input("Enter the column for the Y axis: ", validators=[ColumnValidator(self.csv)])

            if res[1]:
                y_column = res[0]
                break

        plt.scatter(self.csv[x_column], self.csv[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"Scatter Plot of {y_column} vs {x_column}")
        plt.savefig(config["save_path"] + '/scatter_plot.png')

    def export_histogram(self):
        column = input("Enter the column for the histogram: ")

        self.csv[column].plot(kind='hist')
        plt.xlabel(column)
        plt.title(f"Histogram of {column}")
        plt.savefig(config["save_path"] + '/histogram_plot.png')

    def export_pie_chart(self):
        column = input("Enter the column for the pie chart: ")

        self.csv[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title(f"Pie Chart of {column}")
        plt.savefig(config["save_path"] + '/pie_chart_plot.png')

    @menu_item("Show table")
    def show_table(self):
        print(self.csv)
        input()

    @menu_item("Show extremas")
    def show_extremes(self):
        extremes = {}
        for column in self.csv.columns:
            extremes[column] = {
                "min": self.csv[column].min(),
                "max": self.csv[column].max()
            }

        for e in extremes:
            print(e, extremes[e])
        input()

    @menu_item("Show plot")
    def show_plot(self):
        plot_menu = ConsoleMenu("Choose plot type", "Select an option:")
        plot_menu.append_item(FunctionItem("Line Plot", self.show_line_plot))
        plot_menu.append_item(FunctionItem("Bar Chart", self.show_bar_chart))
        plot_menu.append_item(FunctionItem("Scatter Plot", self.show_scatter_plot))
        plot_menu.append_item(FunctionItem("Histogram", self.show_histogram))
        plot_menu.append_item(FunctionItem("Pie Chart", self.show_pie_chart))

        plot_menu.show() 

    def show_line_plot(self):
        pu = PromptUtils(Screen())
        x_column = ''
        while True:
            res = pu.input("Enter the column for the X axis: ", validators=[ColumnValidator(self.csv)])

            if res[1]:
                x_column = res[0]
                break
        
        y_column = ''
        while True:    
            res = pu.input("Enter the column for the Y axis: ", validators=[ColumnValidator(self.csv)])

            if res[1]:
                y_column = res[0]
                break

        plt.plot(self.csv[x_column], self.csv[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"Line Plot of {y_column} vs {x_column}")
        plt.show()

    def show_bar_chart(self):
        category_column = input("Enter the category column: ")
        value_column = input("Enter the value column: ")

        self.csv.groupby(category_column)[value_column].sum().plot(kind='bar')
        plt.xlabel(category_column)
        plt.ylabel(value_column)
        plt.title(f"Bar Chart of {value_column} by {category_column}")
        plt.show()

    def show_scatter_plot(self):
        pu = PromptUtils(Screen())
        x_column = ''
        while True:
            res = pu.input("Enter the column for the X axis: ", validators=[ColumnValidator(self.csv)])

            if res[1]:
                x_column = res[0]
                break
        
        y_column = ''
        while True:    
            res = pu.input("Enter the column for the Y axis: ", validators=[ColumnValidator(self.csv)])

            if res[1]:
                y_column = res[0]
                break

        plt.scatter(self.csv[x_column], self.csv[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"Scatter Plot of {y_column} vs {x_column}")
        plt.show()

    def show_histogram(self):
        column = input("Enter the column for the histogram: ")

        self.csv[column].plot(kind='hist')
        plt.xlabel(column)
        plt.title(f"Histogram of {column}")
        plt.show()

    def show_pie_chart(self):
        column = input("Enter the column for the pie chart: ")

        self.csv[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title(f"Pie Chart of {column}")
        plt.show()

    def run(self):
        self.show()