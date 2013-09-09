import a1
import imageIO as io

castle = io.imread('castle_small.png')
imL, imC = a1.spanish(castle)
io.imwrite(imL, 'L.png')
io.imwrite(imC, 'C.png')
