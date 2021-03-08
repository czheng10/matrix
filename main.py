from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

m1= new_matrix()
m2= new_matrix(rows=4, cols= 0)

#testing add_edge. Adding (1,2,3), (4,5,6) m2 =
print("testing add_edge. Adding (1,2,3), (4,5,6) m2 = ")
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)

#testing ident. m1 =
print("testing ident. m1 = ")
ident(m1)
print_matrix(m1)

#testing Matrix mult. m1*m2 =
print("testing Matrix mult. m1*m2 = ")
matrix_mult(m1,m2)
print_matrix(m2)

#testing Matrix mult. m3 =
print("testing Matrix mult. m3 = ")
m3 = new_matrix(rows=4, cols= 0)
add_edge(m3,1,2,3,4,5,6)
add_edge(m3,7,8,9,10,11,12)
print_matrix(m3)

#testing Matrix mult. m3*m2 =
print("testing Matrix mult. m3*m2 = ")
matrix_mult(m3,m2)
print_matrix(m2)

#draw_lines to create image
color= [255,255,255]
head = new_matrix(rows=4, cols= 0)
add_edge(head, 225,320,0, 255,320,0)
add_edge(head, 255,320,0, 270,300,0)
add_edge(head, 270,300,0, 255,280,0)
add_edge(head, 255,280,0, 225,280,0)
add_edge(head, 225,280,0, 210,300,0)
add_edge(head, 210,300,0, 225,320,0)
draw_lines(head, screen, color )

body = new_matrix(rows=4, cols= 0)
add_edge(body, 225,280,0, 230,140,0)
add_edge(body, 230,140,0, 240,120,0)
add_edge(body, 240,120,0, 250,140,0)
add_edge(body, 250,140,0, 255,280,0)
add_edge(body, 255,280,0, 230,140,0)
add_edge(body, 225,280,0, 250,140,0)
add_edge(body, 270,300,0, 250,140,0)
add_edge(body, 210,300,0, 230,140,0)
draw_lines(body, screen, color )

antenna = new_matrix(rows=4, cols= 0)
add_edge(antenna, 225,320,0, 220,380,0)
add_edge(antenna, 220,380,0, 215,375,0)
add_edge(antenna, 215,375,0, 225,320,0)
add_edge(antenna, 255,320,0, 260,380,0)
add_edge(antenna, 260,380,0, 265,375,0)
add_edge(antenna, 265,375,0, 255,320,0)
draw_lines(antenna, screen, color )

lwing =  new_matrix(rows=4, cols= 0)
add_edge(lwing, 210,300,0, 130,400,0)
add_edge(lwing, 130,400,0, 40,420,0)
add_edge(lwing, 40,420,0, 15,380,0)
add_edge(lwing, 15,380,0, 45,340,0)
add_edge(lwing, 45,340,0, 55,250,0)
add_edge(lwing, 55,250,0, 110,230,0)
add_edge(lwing, 110,230,0, 70,180,0)
add_edge(lwing, 70,180,0, 100,110,0)
add_edge(lwing, 100,110,0, 160,80,0)
add_edge(lwing, 160,80,0, 230,140,0)
draw_lines(lwing, screen, color )

rwing =  new_matrix(rows=4, cols= 0)
add_edge(rwing, 270,300,0, 350,400,0)
add_edge(rwing, 350,400,0, 440,420,0)
add_edge(rwing, 440,420,0, 465,380,0)
add_edge(rwing, 465,380,0, 435,340,0)
add_edge(rwing, 435,340,0, 445,250,0)
add_edge(rwing, 445,250,0, 390,230,0)
add_edge(rwing, 390,230,0, 430,180,0)
add_edge(rwing, 430,180,0, 400,110,0)
add_edge(rwing, 400,110,0, 340,80,0)
add_edge(rwing, 340,80,0, 250,140,0)
draw_lines(rwing, screen, color )

details = new_matrix(rows=4, cols= 0)
add_edge(details, 45,340,0, 130,400,0)
add_edge(details, 435,340,0, 350,400,0)
add_edge(details, 130,400,0, 55,250,0)
add_edge(details, 350,400,0, 445,250,0)
add_edge(details, 130,400,0, 15,380,0)
add_edge(details, 350,400,0, 465,380,0)
add_edge(details, 45, 340,0, 100,340,0)
add_edge(details, 435,340,0, 390,340,0)
add_edge(details, 390,340,0, 270,300,0)
add_edge(details, 390,340,0, 390,230,0)
add_edge(details, 100,340,0, 210,300,0)
add_edge(details, 100,340,0, 110,230,0)
add_edge(details, 40,420,0, 45,340,0)
add_edge(details, 440,420,0, 435,340,0)
add_edge(details, 223,200,0, 110,230,0)
add_edge(details, 223,200,0, 70,180,0)
add_edge(details, 258,200,0, 390,230,0)
add_edge(details, 258,200,0, 430,180,0)
add_edge(details, 210,300,0, 110,230,0)
add_edge(details, 270,300,0, 390,230,0)
add_edge(details, 70,180,0, 160,80,0)
add_edge(details, 430,180,0, 340,80,0)
add_edge(details, 100,110,0, 223,200,0)
add_edge(details, 400,110,0, 258,200,0)
add_edge(details, 110,230,0, 100,110,0)
add_edge(details, 390,230,0, 400,110,0)
add_edge(details, 100,110,0, 230,140,0)
add_edge(details, 250,140,0, 400,110,0)
         
draw_lines(details, screen, color )

display(screen)
save_ppm(screen, 'binary.ppm')
save_ppm_ascii(screen, 'ascii.ppm')
save_extension(screen, 'img.PNG')
