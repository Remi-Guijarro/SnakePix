from PIL import Image 

def inversion_videoNB(img, xs, ys) :
    res = Image.new("L",img.size,"black")
    for y in range (0,ys):
        for x in range (0,xs):
            col=img.getpixel((x,y))
            res.putpixel((x,y),255-col)
    return res


def plusClairNB(img,  xs,  ys) :
    res = Image.new("L",img.size,"black")
    for y in range (0,ys):
        for x in range (0,xs):
            col=img.getpixel((x,y))
            res.putpixel((x,y),int(col+65))
    return res

def deriv1xNB(img,sx,sy) :
    res = Image.new("L",img.size,"black")
    for y in range (0,sx):
        for x in range (0,sy):
            if(x != 0):                
                previousPixel=img.getpixel((x-1,y))
                col=img.getpixel((x,y))
                newPixel = col - previousPixel
                newPixel = convertToviewablePixel(newPixel)
                res.putpixel((x,y),int(newPixel))
    return res

def convertToviewablePixel(p):
    p = troncate(p)
    return p + 128

def troncate(p):
    if(p < -128):
        p = -128
    elif(p > 127):
        p = 127
    return p

def traitV(sx,sy,x,y) :
    res = Image.new("L",(sx,sy),"black")
    for yy in range (0,y):
        res.putpixel((x,(sy-1)-yy),255)
    return res



def mouvement(img1, img2) :
    (xs,ys)=img1.size
    print (xs,ys)
    (xs,ys)=img2.size
    print (xs,ys)
    res = Image.new("L",img1.size,"black")
    for y in range (0,ys):
        for x in range (0,xs):
            col=img1.getpixel ((x,y))-img2.getpixel ((x,y))
            if col<0 :
                col=-col
            res.putpixel((x,y),col)
    return res

