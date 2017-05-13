
for i in range(1,193):
    line = ' <li><a class="swap" href="#"><img src="images/gallery/'
    thumb_name = 'thumb'+ str(i) + '.jpg'
    line+=thumb_name
    line+= '" alt="" /><span><img src="images/gallery/'
    image_name = 'img'+ str(i) +'.jpg'
    line+=image_name
    line+='" height="480" alt="" /></span></a></li>'
    print line
