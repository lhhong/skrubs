import exifread
import urllib

def evaluate(data):
    result = []

    for input in data:
        lat = None
        lon = None
        image_path = input.get("path")
        image = open(image_path, 'rb')
        tags = exifread.process_file(image, details=False)

        gps_latitude = get_if_exist(tags, 'GPS GPSLatitude')
        gps_latitude_ref = get_if_exist(tags, 'GPS GPSLatitudeRef')
        gps_longitude = get_if_exist(tags, 'GPS GPSLongitude')
        gps_longitude_ref = get_if_exist(tags, 'GPS GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = convert_to_degress(gps_latitude)
            if gps_latitude_ref.values[0] != 'N':
                lat = 0 - lat

            lon = convert_to_degress(gps_longitude)
            if gps_longitude_ref.values[0] != 'E':
                lon = 0 - lon
        result.append({"lat":lat, "long":lon})

    return result

def get_if_exist(data, key):
    if key in data:
        return data[key]

    return None

def convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
    :param value:
    :type value: exifread.utils.Ratio
    :rtype: float
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)


tests = [[
    {"path": "https://cis2018-photo-gps.herokuapp.com/images/sample1.jpg"},
    {"path": "https://cis2018-photo-gps.herokuapp.com/images/sample2.jpg"},
    {"path": "https://cis2018-photo-gps.herokuapp.com/images/sample3.jpg"},
    {"path": "https://cis2018-photo-gps.herokuapp.com/images/sample4.jpg"},
    {"path": "https://cis2018-photo-gps.herokuapp.com/images/sample5.jpg"}
]]
