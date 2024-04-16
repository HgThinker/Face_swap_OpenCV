# Face swap OpenCV 

This small project aim to implement a swapping faces method, in which we use module dlib landmark detection .

## Installation

```bash
bash scripts/setup_everything.sh
```

## Usage
### Face swapping picture to picture
- To use this function, you need at least 2 pictures, each contains only 1 face.
- Put your pictures into the 'image' folder to use them.
- Run the command below:

```python
python src/FACE_SWAP/Face_swap_picture.py --source_image_name=<SOURCE_IMAGE_NAME> --des_image_name=<DES_IMAGE_NAME>   
```
- source_image_name: the name of picture you take the face from(E.g. Mickey.png)
- des_image_name: the name of picture you stick the face into(E.g. Donald.jpg)

### Face swapping real-time
- To use this function, you need at least 1 picture which contains only 1 face.
- A webcam(of course)
- Run the command below:

```python
python src/FACE_SWAP/Face_swap_realtime.py --image_name=<IMAGE_NAME> --video_name=<VIDEO_NAME> 
```
- image_name: the name of picture you take the face from(E.g. Jack.png)
- video_name: the name you choose for the output video file (E.g. Funny_face_swaping_clip)
 
***The loop would run until you press the key 'p'***
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
