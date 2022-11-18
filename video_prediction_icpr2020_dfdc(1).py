import torch
from torch.utils.model_zoo import load_url
import matplotlib.pyplot as plt
from scipy.special import expit
import argparse

import sys
sys.path.append('..')

from blazeface import FaceExtractor, BlazeFace, VideoReader
from architectures import fornet,weights
from isplutils import utils

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--in_file', type=str)

args = parser.parse_args()

in_file = args.in_file

threshold = 0.3

"""
Choose an architecture between
- EfficientNetB4
- EfficientNetB4ST
- EfficientNetAutoAttB4
- EfficientNetAutoAttB4ST
- Xception
"""
net_model = 'EfficientNetB4ST'

"""
Choose a training dataset between
- DFDC
- FFPP
"""
train_db = 'DFDC'
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
face_policy = 'scale'
face_size = 224
frames_per_video = 32
#model_url = weights.weight_url['{:s}_{:s}'.format(net_model,train_db)]
#print(model_url)
net = getattr(fornet,net_model)().eval().to(device)
# print(net)
#net.load_state_dict(load_url(model_url,map_location=device,check_hash=True))
model_path = "/home/soumya/deepfake_detect/icpr2020dfdc/models/EfficientNetB4ST_DFDC_bestval-86f0a0701b18694dfb5e7837bd09fa8e48a5146c193227edccf59f1b038181c6.pth"
net.load_state_dict(torch.load(model_path))
transf = utils.get_transformer(face_policy, face_size, net.get_normalizer(), train=False)
facedet = BlazeFace().to(device)
facedet.load_weights("./blazeface/blazeface.pth")
facedet.load_anchors("./blazeface/anchors.npy")
videoreader = VideoReader(verbose=False)
video_read_fn = lambda x: videoreader.read_frames(x, num_frames=frames_per_video)
face_extractor = FaceExtractor(video_read_fn=video_read_fn,facedet=facedet)
import json
import requests
while True:
            
      response = requests.get("http://10.244.0.178:5000/get_media_id")
      print("<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
      get_media_id_data = response.json()
      print("<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
      print(get_media_id_data.get('media_id'))
      form_data={"id":get_media_id_data.get('media_id')}
      res=requests.post("http://10.244.0.178:5000/get_media_of_id",data=form_data)
      print("<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
      with open("res.mp4","wb") as f:
            f.write(res.content)    
      vidpath = "res.mp4"
      vid_faces = face_extractor.process_video(vidpath)
      # vid_faces = face_extractor.process_video(in_file)
      faces_t = torch.stack( [ transf(image=frame['faces'][0])['image'] for frame in vid_faces if len(frame['faces'])] )
      with torch.no_grad():
            faces_pred = net(faces_t.to(device)).cpu().numpy().flatten()
      print('Average score for given video with threshold: {:.4f}'.format(expit(faces_pred.mean())))
      confidence_percentage=faces_pred.mean()
      if (faces_pred.mean()<threshold):
            print("Real")
            result="Real"
      else:
            print("Fake")
            result="Fake"
      form_data={"id": get_media_id_data.get('media_id'), "status":"result", "confidence_percentage":faces_pred.mean()}
      res=requests.post("http://10.244.0.178:5000/update_media_id_result_status", data=form_data)    
      print(res.content)    




