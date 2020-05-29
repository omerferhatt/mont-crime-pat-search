# Library imports
import numpy as np
import pandas as pd
import shapefile


def read_shp(path):
    """
    Converts shape files into data frames

    :param path: Location of shape files. Don't add file extensions
    :return: Pandas Dataframe object
    """

    file_group = path
    sf = shapefile.Reader(file_group, encoding="latin1")
    bbox = sf.bbox

    shapes = sf.shapes()
    shape_recs = sf.shapeRecords()
    # Reads numerical values
    loc_0 = np.array([float(d.points[0][1]) for d in shapes], dtype=np.float32)
    loc_1 = np.array([float(d.points[0][0]) for d in shapes], dtype=np.float32)
    # Crime status and date information
    sit = np.array([d.record[0] for d in shape_recs], dtype=str)
    date = np.array([d.record[2] for d in shape_recs])
    # Creating data frame to working with data easier
    cols = ["Location1", "Location2", "Situation", "Date"]
    data = np.array([loc_0, loc_1, sit, date]).T
    df = pd.DataFrame(data=data, columns=cols)
    return df, bbox

# Gets values from data frame into numpy array
def get_values(df, dtype):
    return df.to_numpy()[:, :2].astype(dtype)