from math import ceil
import FreeCAD
import Part

class Object:
    __shape = None

    def __init__(self, path):
        """
        Get a Part object from a path and set self.__shape with the FreeCAD Part object
        @param {string} path    File path
        """
        self.__shape = Part.Shape()
        self.__shape.read(path)
        self.__shape.tessellate(1)

    def volume(self):
        """
        Get the volume of the self.__shape
        @return {int} Object volume in mm3 multiplied by 100
        """
        if not self.__shape:
            return 0

        return ceil(self.__shape.Volume * 100)

    def boundbox_dimensions(self):
        """
        Get the dimendion of the boundbox of the shape
        @return {dict}                  Dimensions
                    {dict} x            Dict with max, min and length. All multiplied by 100
                        {int} max       Max value of the dimension
                        {int} min       Min value of the dimension
                        {int} length    Dimension length
                    {dict} y            Dict with max, min and length. All multiplied by 100
                        {int} max       Max value of the dimension
                        {int} min       Min value of the dimension
                        {int} length    Dimension length
                    {dict} z            Dict with max, min and length. All multiplied by 10
                        {int} max       Max value of the dimension
                        {int} min       Min value of the dimension
                        {int} length    Dimension length
        """
        if not self.__shape:
            return {'x': 0, 'y': 0, 'z': 0}

        bb = self.__shape.BoundBox

        return {
            'x': {
                'max': ceil(bb.XMax * 100),
                'min': ceil(bb.XMin * 100),
                'length': ceil((bb.XMax - bb.XMin) * 100),
            },
            'y': {
                'max': ceil(bb.YMax * 100),
                'min': ceil(bb.YMin * 100),
                'length': ceil((bb.YMax - bb.YMin) * 100),
            },
            'z': {
                'max': ceil(bb.ZMax * 100),
                'min': ceil(bb.ZMin * 100),
                'length': ceil((bb.ZMax - bb.ZMin) * 100),
            },
        }

    def boundbox_volume(self):
        """
        Get the volume of the boundbox of self.__shape
        @return {int} object bounbox volume in mm3 multiplied by 100
        """
        if not self.__shape:
            return 0

        bb = self.__shape.BoundBox

        vol = (bb.XMax - bb.XMin) * (bb.YMax - bb.YMin) * (bb.ZMax - bb.ZMin)

        return ceil(vol * 100)

    def raw_material_volume(self):
        """
        Get the volume of the raw material of self.__shape
        @return {int} object bounbox volume in mm3 multiplied by 100
        """
        if not self.__shape:
            return 0

        bb = self.__shape.BoundBox

        vol = (bb.XMax - bb.XMin + 10) * (bb.YMax - bb.YMin + 10) * (bb.ZMax - bb.ZMin + 10)

        return ceil(vol * 100)

    def get_all_info(self):
        """
        Get all infos of the object
        @return {dict}  Volume, raw material volume and dimensions
        """
        return {
            'volume': self.volume(),
            'raw_material_volume': self.raw_material_volume(),
            'boundbox_dimensions': self.boundbox_dimensions(),
        }
