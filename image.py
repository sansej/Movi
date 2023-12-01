import imageio 
from PIL import Image
import numpy

class ImageEditor:
    """
    Image crop and convert image to video
    """

    def crop_image(input_path, output_path, resolution = (720, 1280)):
        """
        Parameters
        -----------
        input_path - path to source image ``*.JPG`` ``*.PNG``

        output_path - path to modified image ``*.JPG`` ``*.PNG``

        resolution - final image resolution, default ``720*1280``
        """
        original_image = Image.open(input_path).crop()
        target_width, target_height = resolution
        if original_image.width >= target_width and original_image.height >= target_height:
            crop_box = ((original_image.width - target_width) // 2, (original_image.height - target_height) // 2,
                            (original_image.width + target_width) // 2, (original_image.height + target_height) // 2)
            cropped_image = original_image.crop(crop_box)
            cropped_image.save(output_path)
            print(f"Image cropped ({cropped_image.width} {cropped_image.height}) and saved to {output_path}")
            return
        else:
            print(f"Image resolution ({original_image.width}x{original_image.height}) is less than {target_width}x{target_height}.")
    
    def ken_burns_effect_video(image_path, output_path, duration=10, zoom_factor=1.4, reverse=False, fps=30):
        """
        Parameters
        -----------
        image_path - path to source image ``*.JPG`` ``*.PNG``

        output_path - path to the created video file ``*.MP4``

        duration - duration of the created video in ``seconds``, default ``10s``

        zoom_factor - zoom factor, default ``1.4``

        reverse -  zoom in ``False`` | zoom out ``True``

        fps - number of frames per second, , default ``30``
        """
        img = Image.open(image_path)
        new_width = (img.width // 16) * 16
        new_height = (img.height // 16) * 16
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        frames = []
        long = duration * fps
        for i in range(long):
            current_zoom = 1 + (zoom_factor - 1) * i / long
            position = (
                (img.width - img.width * current_zoom) / 2,
                (img.height - img.height * current_zoom) / 2
            )
            frame = img.resize((int(img.width * current_zoom), int(img.height * current_zoom)), Image.Resampling.LANCZOS)
            canvas = Image.new("RGB", img.size, "black")
            canvas.paste(frame, box=(int(position[0]), int(position[1])))
            frames.append(canvas)
        if reverse:
            frames = frames[::-1]
        with imageio.get_writer(output_path, fps=fps) as writer:
            for frame in frames:
                frame_array = numpy.array(frame)
                writer.append_data(frame_array)
        print(f'{output_path} video file created')