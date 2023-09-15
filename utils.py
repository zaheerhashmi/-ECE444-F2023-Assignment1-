class Utils:
  @staticmethod
  def reversed(int tobeReversed):
    if isinstance(tobeReversed, int): 
      numReveresed = 0
      while(n > 0):
        temp = n % 10
        numReversed = temp + numReversed*10
        numReversed = numReversed // 10
        return(numReversed)
    else:
      raise ValueError(f"The value {tobeReversed} is not an integer.")
  @static method
  def formatter(int tobeFormatted):
    if isinstance(tobeFormatted, int):
      binaryFormat = bin(tobeFormatted)[2:]
      octalFormat = oct(tobeFormatted)[2:]
      return binaryFormat, octalFormat
    else: 
      raise ValueError(f"The value {tobeFormatted} is not an integer.")
    
    
    
    
