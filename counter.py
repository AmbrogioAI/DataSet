import os 

def countFileInDir(path):
    files = os.listdir(path)
    #percentage = computePercentageOfFilesInDir(files)
    return len(files)#, percentage

def computePercentageOfFilesInDir(files):
    extensions = {}
    for file in files:
        extension = file.split('.')[-1]
        if extension in extensions:
            extensions[extension] += 1
        else:
            extensions[extension] = 1
            
    total = sum(extensions.values())
    percentages = {}
    for key, value in extensions.items():
        percentages[key] = value / total * 100
    
    return percentages

# Utility to count the quantity of files foreach class
if __name__ == '__main__':
    paths = ["sportivo","elegante","casual"]
    sum = 0
    for path in paths:
        #count, percentage = countFileInDir(path)
        count = countFileInDir(path)
        sum = count + sum
        print(f"Path: {path}, Count: {count}")
    print(f"Total of images: {sum}")