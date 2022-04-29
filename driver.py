import utils

def main():
    # Grab the collection from the mongo database
    collection = utils.get_collection()

    # Get a list of all the plot ids to query for
    my_plot_ids = utils.get_plot_ids(collection)

    """TBD: Loop to grab these values for every report in the collection"""
    # Loop through the plot ids and get the plot
    my_plot = utils.get_plot(collection, plot_id=my_plot_ids[0])

    # Loop through the treatment ids and get the treatment
    my_treatment_ids = list(my_plot.keys() - ['_id'])
    my_treatment = my_plot[my_treatment_ids[0]]
    
    # Loop through the iteration ids and get the iteration
    my_iteration_ids = list(my_treatment.keys())
    my_iteration = my_treatment[my_iteration_ids[0]]

    # Loop through the report ids and get the report
    my_report_ids = list(my_iteration.keys())
    my_report_id = my_report_ids[1] # Grab CARBREPT
    my_report = my_iteration[my_report_id]

    my_year_ids = list(my_report.keys())
    my_year = my_report[my_year_ids[0]]

    my_carbrept_ids = list(my_year.keys())
    total_carb = my_year[my_carbrept_ids[4]]
    print("Found total carb for plot_id: {}".format(my_plot_ids[0]))
    print("Treatment: {}".format(my_treatment_ids[0]))
    print("Iteration: {}".format(my_iteration_ids[0]))
    print("Report: {}".format(my_report_id))
    print("Year: {}".format(my_year_ids[0]))
    print("Total carb: {}".format(total_carb))

if __name__ == "__main__":
    main()