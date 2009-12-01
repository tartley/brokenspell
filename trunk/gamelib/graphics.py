
from glob import glob
from os.path import join

from pyglet.image import load, SolidColorImagePattern
from pyglet.image.atlas import TextureAtlas


IMAGES_DIR = join('data', 'images')

# blank image spacer to prevent adjacent images in the atlas from bleeding
# into each other
SPACER = SolidColorImagePattern((0, 0, 0, 0)).create_image(1024, 1)


def set_anchor(image):
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


class Graphics(object):

    def __init__(self):
        self.atlas = TextureAtlas(width=1024, height=512)
        blank = SolidColorImagePattern((0, 0, 0, 0)).create_image(1024, 1)
        self.atlas.add(blank)


    def _split_filename(self, filename):
        r"""
        Splits filename 'blah\file-X.ext' into tuple ('file', X), where X
        is any integer. Returns ('file', None) if filename does not end in
        hyphen followed by integer.
        """
        basename = filename[len(IMAGES_DIR) + 1:-4]
        name = basename
        number = None
        hyphen = basename.rfind('-')
        if hyphen != -1:
            try:
                number = int(basename[hyphen + 1:])
                name = basename[:hyphen]
            except ValueError:
                pass
        return name, number


    def _split_image(self, image, num_frames):
        """
        Expects an image to contain 1 or more frames, as a horizontal row of
        equally sized regions. Splits the given image into its constituent
        frames, returning them as a list of texture regions.
        """
        frames = []
        frame_width = image.width / num_frames
        for i in xrange(0, num_frames):
            region = image.get_region(
                frame_width * i, 0, frame_width, image.height)
            set_anchor(region)
            frames.append(region)
        return frames


    def load(self):
        """
        Loads all files in images directory, making them available as
        self.images[filename]. Each entry in that dictionary is a list of X
        frames, where X, if not 1, is indicated by the filename ending in
        '-X.png'
        """
        images = {}
        for filename in glob('%s/*.png' % (IMAGES_DIR)):
            self.atlas.add(SPACER)
            region = self.atlas.add(load(filename))
            name, num_frames = self._split_filename(filename)
            if num_frames:
                images[name] = self._split_image(region, num_frames)
            else:
                images[name] = [region]
        return images

