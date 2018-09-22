import exifread
def evaluate(data):
    result = []
    for input in data:
        image_path = input.get("path")
        image = open(image_path, 'rb')
        tags = exifread.process_file(f)
        results.append(tags)
    return results
    #

tests = [
    {path: "/images/sample1.jpg"},
    {path: "/images/sample2.jpg"},
    {path: "/images/sample3.jpg"},
    {path: "/images/sample4.jpg"},
    {path: "/images/sample5.jpg"}
]
