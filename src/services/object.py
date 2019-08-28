import FreeCAD
import Part

class Object:
    __obj = None

    def __init__(self, path):
        """ Get a Part object from a path and set self.__obj
            with the FreeCAD Part object
        Parameters
        ----------
        path: str
            path where the file is located
        """
        self.__obj = Part.read(path)

    def volume(self):
        """ Get the volume of the self.__obj
        Return
        ----------
        float
            object volume in mm3
            rounded with 2 decimal places
        """
        if not self.__obj:
            return round(0, 2)

        return round(self.__obj.Volume, 2)

    def boundbox_volume(self):
        """ Get the volume of the boundbox of self.__obj
        Return
        ----------
        float
            object bounbox volume in mm3
            rounded with 2 decimal places
        """
        if not self.__obj:
            return round(0, 2)

        bb = self.__obj.BoundBox

        vol = (bb.XMax - bb.XMin) * (bb.YMax - bb.YMin) * (bb.ZMax - bb.ZMin)

        return round(vol, 2)

    def raw_material_volume(self):
        """ Get the volume of the raw material of self.__obj
        Return
        ----------
        float
            object bounbox volume in mm3
            rounded with 2 decimal places
        """
        if not self.__obj:
            return round(0, 2)

        bb = self.__obj.BoundBox

        vol = (bb.XMax - bb.XMin + 10) * (bb.YMax - bb.YMin + 10) * (bb.ZMax - bb.ZMin + 10)

        return round(vol, 2)

def mm3_to_cm3(volume):
    """ Convert volume from mm3 to cm3
    Parameters
    ----------
    volume: float
        mm3 volume
        
    Return
    ----------
    float
        cm3 volume
    """
    return round(volume/1000, 2)
