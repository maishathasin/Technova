from transformers import pipeline


def model(image_path):
    model = pipeline("object-detection")
    arr = model(image_path)
    count =  len(arr)
    di = {}
    for i in arr:
        value = 0
        label = i['label']
        if label not in di:
            value += 1
            di[label] = value
        else:
            di[label] = di[label] + 1
    return di 

        
    

    
    
    
    