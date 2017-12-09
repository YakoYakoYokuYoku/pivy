"""
This is an example from the Inventor Mentor,
chapter 6, example 3.

This example renders arguments as text within an
ExaminerViewer.  It is a little fancier than 6.2.
"""

import sys

from pivy.gui.qt import *
from pivy.coin import *
from pivy.quarter import *

def main():
    # Initialize Inventor and Qt
    app = QApplication(sys.argv)
    viewer = QuarterWidget()

    root = SoGroup()

    # Set up camera
    myCamera = SoPerspectiveCamera()
    myCamera.position = (0, -(len(sys.argv) - 1) / 2, 10)
    myCamera.nearDistance = 5.0
    myCamera.farDistance = 15.0
    root += myCamera

    # Let's make the front of the text white,
    # and the sides and back shiny yellow
    myMaterial = SoMaterial()
    # diffuse
    colors = [SbColor()] * 3
    colors[0] = SbColor(1, 1, 1)
    colors[1] = SbColor(1, 1, 0)
    colors[2] = SbColor(1, 1, 0)
    myMaterial.diffuseColor.setValues(0, 3, colors)

    # specular
    colors[0].setValue(1, 1, 1)
    """
    # Note: Inventor 2.1 doesn't support multiple specular colors.
    # colors[1].setValue(1, 1, 0)
    # colors[2].setValue(1, 1, 0)
    # myMaterial.specularColor.setValues(0, 3, colors)
    """
    myMaterial.specularColor.setValue(colors[0])
    myMaterial.shininess.setValue(.1)
    root += myMaterial

    # Choose a font likely to exist.
    myFont = SoFont()
    myFont.name = "Times" # "Times-Roman"
    root += myFont

    # Specify a beveled cross-section for the text
    myProfileCoords = SoProfileCoordinate2()
    coords = [SbVec2f()] * 4
    coords[0] = SbVec2f(.00, .00)
    coords[1] = SbVec2f(.25, .25)
    coords[2] = SbVec2f(1.25, .25)
    coords[3] = SbVec2f(1.50, .00)
    myProfileCoords.point.setValues(0, 4, coords)
    root += myProfileCoords

    myLinearProfile = SoLinearProfile()
    index = (0, 1, 2, 3)
    myLinearProfile.index.setValues(0, 4, index)
    root += myLinearProfile

    # Set the material binding to PER_PART
    myMaterialBinding = SoMaterialBinding()
    myMaterialBinding.value = SoMaterialBinding.PER_PART
    root += myMaterialBinding

    # Add the text
    myText3 = SoText3()
    myText3.string = "Beveled Text"
    myText3.justification = SoText3.CENTER
    myText3.parts = SoText3.ALL

    root += myText3
	
    viewer.setSceneGraph(root)
    viewer.setWindowTitle("Complex 3D Text")
    viewer.show()
    viewer.viewAll()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()