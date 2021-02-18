import PIL.Image as Image
import argparse
import io



def make_img(img: Image, width: int, height: int) -> image_pb2.ProtoImg:
    """
    Creates ProtoImg object from regular image.
    """
    return image_pb2.ProtoImg(color=0 if is_gray(img) else 1,
                              data=img2bytes(img, img.format).getvalue(),
                              width=width,
                              height=height)


def img2bytes(img: Image, fmt: str) -> io.BytesIO:
    """
    Converts Image object into a bytestream.
    """
    bytes_io = io.BytesIO()
    img.save(bytes_io, format=fmt)
    return bytes_io


def bytes2img(bytestr: bytes) -> Image:
    """
    Converts bytestream into an Image object.
    """
    return Image.open(io.BytesIO(bytestr))


def get_channel_diff(c1: float, c2: float) -> float:
    """
    Gets the absolute difference between two channels.
    """
    return c1 - c2 if c1 >= c2 else c2 - c1


def is_gray(img: Image, threshold: float = .01) -> bool:
    """
    Determines if the input Image is grayscale or RGB.
    """
    width, height = img.size
    if img.mode == 1:
        return True
    for x in range(width):
        for y in range(height):
            r, g, b = list(img.getpixel((x, y)))[:3]
            rg_below_thresh = get_channel_diff(r, g) <= threshold
            rb_below_thresh = get_channel_diff(r, b) <= threshold
            gb_below_thresh = get_channel_diff(g, b) <= threshold
            if not (r == g == b) or not all([rg_below_thresh,
                                             rb_below_thresh,
                                             gb_below_thresh]):
                return False
    return True


def get_cmd_args(flag):
    """
    Processes input arguments from the command line.
    """
    parser = argparse.ArgumentParser(description="Command line parser")
    if flag == "client":
        parser.add_argument("--port", required=True, help="Port used by the client to communicate with the server.")
        parser.add_argument("--host", required=True, help="Host client IP Address.")
        parser.add_argument("--input", required=True, help="Input path specifying the input directory.")
        parser.add_argument("--output", required=True, help="Output path specifying the output directory.")
        parser.add_argument("--rotate", help="NONE, NINETY_DEG, ONE_EIGHTY_DEG, TWO_SEVENTY_DEG")
        parser.add_argument("--mean", action="store_true", help="Mean invokes a blur filter over the input image.")
    elif flag == "service":
        parser.add_argument("--host", required=True, help="The host IP address.")
        parser.add_argument("--port", required=True, help="The exposed port number on host machine.")
    return vars(parser.parse_args())
