from rich.console import Console
import time

console = Console()

def clear():
    console.clear()

def type_out_banner():
    frames = [
        r"""
       
MM 
MM 
MM 
MM 
MM 
MM 
MM 
MM 
MM 
MM 
        """,
        r"""
    ,,,,MM 
  .d' **MM 
  dM`   MM 
 mMMmm  MM 
  MM    MM 
  MM    MM 
  MM    MM 
.JMML.  MM 
        MM 
        MM  
        """,
        r"""
    ,,,,       MM 
  .d' **       MM 
  dM`          MM 
 mMMmm ,6*Yb.  MM 
  MM  8)   MM  MM 
  MM   ,pm9MM  MM 
  MM  8M   MM  MM 
.JMML.`Moo9^Yo.MM 
               MM 
               MM """,
        r"""
    ,,,,               MM 
  .d' **               MM 
  dM`                  MM 
 mMMmm ,6*Yb.  ,p6*bo  MM 
  MM  8)   MM 6M'  OO  MM 
  MM   ,pm9MM 8M       MM 
  MM  8M   MM YM.    , MM 
.JMML.`Moo9^Yo.YMbmd'  MM 
                       MM 
                       MM """,
        r"""
    ,,,,                        MM 
  .d' **                        MM 
  dM`                           MM 
 mMMmm ,6*Yb.  ,p6*bo   .gP*Ya  MM 
  MM  8)   MM 6M'  OO  ,M'   Yb MM 
  MM   ,pm9MM 8M       8M****** MM 
  MM  8M   MM YM.    , YM.    , MM 
.JMML.`Moo9^Yo.YMbmd'   `Mbmmd' MM 
                                MM 
                                MM """,
        r"""
    ,,,,                        ,,        MM 
  .d' **                       *MM        MM 
  dM`                           MM        MM 
 mMMmm ,6*Yb.  ,p6*bo   .gP*Ya  MM,dMMb.  MM 
  MM  8)   MM 6M'  OO  ,M'   Yb MM    `Mb MM 
  MM   ,pm9MM 8M       8M****** MM     M8 MM 
  MM  8M   MM YM.    , YM.    , MM.   ,M9 MM 
.JMML.`Moo9^Yo.YMbmd'   `Mbmmd' P^YbmdP'  MM 
                                          MM 
                                          MM """,
        r"""
    ,,,,                        ,,                  MM 
  .d' **                       *MM                  MM 
  dM`                           MM                  MM 
 mMMmm ,6*Yb.  ,p6*bo   .gP*Ya  MM,dMMb.   ,pW*Wq.  MM 
  MM  8)   MM 6M'  OO  ,M'   Yb MM    `Mb 6W'   `Wb MM 
  MM   ,pm9MM 8M       8M****** MM     M8 8M     M8 MM 
  MM  8M   MM YM.    , YM.    , MM.   ,M9 YA.   ,A9 MM 
.JMML.`Moo9^Yo.YMbmd'   `Mbmmd' P^YbmdP'   `Ybmd9'  MM 
                                                    MM 
                                                    MM""",
        r"""
    ,,,,                        ,,                       MM 
  .d' **                       *MM                  mm   MM 
  dM`                           MM                  MM   MM 
 mMMmm ,6*Yb.  ,p6*bo   .gP*Ya  MM,dMMb.   ,pW*Wq.mmMMmm MM 
  MM  8)   MM 6M'  OO  ,M'   Yb MM    `Mb 6W'   `Wb MM   MM 
  MM   ,pm9MM 8M       8M****** MM     M8 8M     M8 MM   MM 
  MM  8M   MM YM.    , YM.    , MM.   ,M9 YA.   ,A9 MM   MM 
.JMML.`Moo9^Yo.YMbmd'   `Mbmmd' P^YbmdP'   `Ybmd9'  `MbmoMM 
                                                         MM 
                                                         MM""",
        r"""
    ,,,,                        ,,                        
  .d' **                       *MM                  mm    
  dM`                           MM                  MM    
 mMMmm ,6*Yb.  ,p6*bo   .gP*Ya  MM,dMMb.   ,pW*Wq.mmMMmm  
  MM  8)   MM 6M'  OO  ,M'   Yb MM    `Mb 6W'   `Wb MM    
  MM   ,pm9MM 8M       8M****** MM     M8 8M     M8 MM    
  MM  8M   MM YM.    , YM.    , MM.   ,M9 YA.   ,A9 MM    
.JMML.`Moo9^Yo.YMbmd'   `Mbmmd' P^YbmdP'   `Ybmd9'  `Mbmo"""
    ]

    for frame in frames:
        console.print(frame, style="bold blue", markup=False)
        time.sleep(0.15)
        clear()


def print_banner():
 console.print("""
    ,,,,                        ,,                  
  .d' **                       *MM                  mm    
  dM`                           MM                  MM    
 mMMmm ,6*Yb.  ,p6*bo   .gP*Ya  MM,dMMb.   ,pW*Wq.mmMMmm  
  MM  8)   MM 6M'  OO  ,M'   Yb MM    `Mb 6W'   `Wb MM    
  MM   ,pm9MM 8M       8M****** MM     M8 8M     M8 MM    
  MM  8M   MM YM.    , YM.    , MM.   ,M9 YA.   ,A9 MM    
.JMML.`Moo9^Yo.YMbmd'   `Mbmmd' P^YbmdP'   `Ybmd9'  `Mbmo""", style="bold blue", markup=False)
