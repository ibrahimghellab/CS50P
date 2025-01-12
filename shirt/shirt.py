import sys
from PIL import Image
from PIL import ImageOps

if(len(sys.argv)<2):
    sys.exit("Too few command-line arguments")
elif (len(sys.argv)>3):
    sys.exit("Too many command-line arguments")
else:
    extensions=[".png",".jpg",".jpeg"]
    input=sys.argv[1]
    output=sys.argv[2]
    if not (input.lower().endswith(tuple(extensions))):
        sys.exit("Invalid input")
    elif not(output.lower().endswith(tuple(extensions))):
        sys.exit("Invalid output")
    else:
        if(input[-3:]!=output[-3:] or input[-4:]!=output[-4:]):
            print(input[-3:])
            sys.exit("Input and output have different extensions")
        else:
            try:
                img=Image.open(input)
                mask=Image.open("shirt.png")
            except FileNotFoundError:
                sys.exit("Input does not exist")
            else:
                img=ImageOps.fit(image=img,size=mask.size)
                img.paste(mask,(0,0),mask)
                img.save(output)




