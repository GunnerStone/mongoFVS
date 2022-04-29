import pymongo

def get_plot_ids(collection):
    plot_ids = collection.find().distinct('_id')
    return plot_ids