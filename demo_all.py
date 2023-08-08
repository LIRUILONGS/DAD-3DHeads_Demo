#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   demo_all.py
@Time    :   2023/08/08 05:36:27
@Author  :   Li Ruilong
@Version :   1.0
@Contact :   liruilonger@gmail.com
@Desc    :   批量人脸处理
"""

# here put the import lib



from functools import partial
from collections import namedtuple
import os
from fire import Fire
from pytorch_toolbelt.utils import read_rgb_image
from imutils import paths


from predictor import FaceMeshPredictor
from demo_utils import (
    draw_landmarks,
    draw_3d_landmarks,
    draw_mesh,
    draw_pose,
    get_mesh,
    get_flame_params,
    get_output_path,
    MeshSaver,
    ImageSaver,
    JsonSaver,
)

DemoFuncs = namedtuple(
    "DemoFuncs",
    ["processor", "saver"],
)

demo_funcs = {
    "68_landmarks": DemoFuncs(draw_landmarks, ImageSaver),
    "191_landmarks": DemoFuncs(partial(draw_3d_landmarks, subset="191"), ImageSaver),
    "445_landmarks": DemoFuncs(partial(draw_3d_landmarks, subset="445"), ImageSaver),
    "head_mesh": DemoFuncs(partial(draw_mesh, subset="head"), ImageSaver),
    "face_mesh": DemoFuncs(partial(draw_mesh, subset="face"), ImageSaver),
    "pose": DemoFuncs(draw_pose, ImageSaver),
    "3d_mesh": DemoFuncs(get_mesh, MeshSaver),
    "flame_params": DemoFuncs(get_flame_params, JsonSaver)
}


def demo(
    input_image_path: str = 'X:\\face\\res\\msr\\',
    outputs_folder: str = "outputs",
    type_of_output: str = "head_mesh",
) -> None:
    """
    @Time    :   2023/08/08 05:39:17
    @Author  :   liruilonger@gmail.com
    @Version :   1.0
    @Desc    :   图片为探头拿到的图片，图片名字为： 3f2b0e3d86c34690b1c71918bab08980__192.168.1.189.jpg
                 生成图片保存到了对应的文件
                 Args:
                   
                 Returns:
                   void
    """
    

    os.makedirs(outputs_folder, exist_ok=True)
    for fp in paths.list_images("X:\\face\\res\\msr\\"):
        # Preprocess and get predictions.
        image = read_rgb_image(fp)
        predictor = FaceMeshPredictor.dad_3dnet()
        predictions = predictor(image)


        # Get the resulting output.
        result = demo_funcs[type_of_output].processor(predictions, image)
        # Save the demo output.
        saver = demo_funcs[type_of_output].saver()  # instantiate the Saver
        #output_path = get_output_path(fp, outputs_folder, type_of_output, saver.extension)
        fname  =  os.path.basename(fp)
        ip = str(fname).split("__")[1]
        ip = ip.split(".jpg")[0]
        path = "./images/face_z/" + ip + "/" + fname
        print(path)
        saver(result,path )


if __name__ == "__main__":

    Fire(demo)
