import pymongo

def get_plot(collection, plot_id):
    # collection.find returns a cursor object
    # [0] is used to get the first element of the cursor
    plot = collection.find({'_id': plot_id})[0]
    return plot
