
from Colors import cl

def MapFlatlands(startLocation, location):
    flatlandsList = [startLocation, "the town", "the flatlands",
    "the forest", "the mountains", "the islands", "the castle","Green Land","The Dessert","The Lake"]
    
    a = []
    for i in range(0,len(flatlandsList)):
        a.append(" ")
        if location == flatlandsList[i] :
            a[i] = f"{cl.RED}X{cl.RESET}" 

    print (f'''
                       ,-.^._                 _
                     .'The Castle .        ,' ;
          /`-.  ,----'   . {a[6]}   `-.   _  ,-.,
       _.'   `--'         .       `-' '-'      ;
      :  The Lake    . . The Mountains         ;__,-.
      ,' . {a[10]}      . .        {a[5]} .              ;_,-',. ,--.
     :   .       .               .      . .Islands--```    `--'
     :  The Dessert              .     .    {a[4]} ;
     :    {a[9]}                  .   .      :
     ;       .                    . .       :
    (         .               The Forest    ;
     `-.       .               . .{a[3]}      ,'
       ;    Green Land        .              :
     .'         {a[8]}      .         . .-._,'
   .'               .     .          `.
_.' The Town . . The FlatLand       .__;
`._     {a[1]}      . {a[2]}             ;
   `.              .               :..'
     `.           .    ,..__,---._;   
       `-.__Camp Fire ;               
            `.--.{a[0]} ;             

''') 

# MAP:
#                                         
#                                                              The Lake        The Castle
#                                  N                               I                I
#                                W + E                             I                I
#                                  S                          The Dessert --- The Mountains
#                                                                  I                I        
#                                                                  I                I
#                                                             Green Land            I
#                                                                  I                I
#                                                                  I                I
#                                                The Town --- The Flatlands --- The Forest --- The Islands
#                                                                  I
#                                                                  I
#                                                             Starting Area
#                                         
#