"""
Find all images for the slider
"""
import os


def process_info(info, site):
    """
    Add images in the slider path to the info
    """
    slider_dir =  site['slider_dir']
    files = [os.path.join(slider_dir, l)
             for l in sorted(os.listdir(slider_dir))]
    images = [l for l in files if os.path.isfile(l)]
    info['slider_images'] = images
