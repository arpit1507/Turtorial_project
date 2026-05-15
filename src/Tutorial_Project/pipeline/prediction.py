import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        model= load_model("model/model.h5")

        imagename=self.filename
        test_image=image.load_img(imagename,target_size=(224,224))
        test_image=image.img_to_array(test_image)
        test_image=np.expand_dims(test_image,axis=0)
        result=np.argmax(model.predict(test_image),axis=1)
        print(result)

        if result[0]==0:
            prediction="adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib"
        elif result[0]==1:
            prediction="large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa"
        elif result[0]==2:
            prediction="normal"
        else:
            prediction="squamous.cell.carcinoma_left.hilum_T3_N1_M0_IIIa"
    
        return [{"image" : prediction}]
