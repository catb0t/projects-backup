import bitfile
EOF_CHAR=256
PRECISION=16
MSB_MASK=((1<<(PRECISION-1))-1)
MAX_PROBABILITY=(1<<(PRECISION-2))
class ArithmeticCodeError(Exception):
 pass
class ArithmeticCode:
 def __init__(self,static=True):
  self._lower=0
  self._upper=0xFFFF
  self._code=0
  self._underflow_bits=0
  self._ranges=[0 for i in range(self.upper(EOF_CHAR)+1)]
  self._cumulative_prob=0
  self._infile=None
  self._outfile=None
  self._static_model=static
 @staticmethod
 def mask_bit(x):
  return(1<<(PRECISION-(1+x)))
 @staticmethod
 def lower(c):
  if type(c)==str:
   return ord(c)
  return c
 @staticmethod
 def upper(c):
  if type(c)==str:
   return ord(c)+1
  return c+1
 def encode_file(self,input_file_name,output_file_name):
  if(self._infile is not None)or(self._outfile is not None):
   raise ValueError('I/O operation on opened file.')
  if self._static_model:
   self._infile=open(input_file_name,'rb')
   self.build_probability_range_list()
   self._infile.seek(0)
   self._outfile=bitfile.BitFile()
   self._outfile.open(output_file_name,'wb')
   self.write_header()
  else:
   self.initialize_adaptive_probability_range_list()
   self._infile=open(input_file_name,'rb')
   self._outfile=bitfile.BitFile()
   self._outfile.open(output_file_name,'wb')
  c=self._infile.read(1)
  while(c!=''):
   self.apply_symbol_range(c)
   self.write_encoded_bits()
   c=self._infile.read(1)
  self._infile.close()
  self.apply_symbol_range(EOF_CHAR)
  self.write_encoded_bits()
  self.write_remaining()
  self._outfile.close()
 def build_probability_range_list(self):
  if self._infile is None:
   raise ArithmeticCodeError('No input file opened for encoding.')
  count_array=[0 for i in range(EOF_CHAR)]
  c=self._infile.read(1)
  while(c!=''):
   count_array[ord(c)]+=1
   c=self._infile.read(1)
  total_count=sum(count_array)
  if total_count>=MAX_PROBABILITY:
   rescale_value=(total_count/MAX_PROBABILITY)+1
   for index,value in enumerate(count_array):
    if value>rescale_value:
     count_array[index]=value/rescale_value
    elif value!=0:
     count_array[index]=1
  self._ranges=[0]+count_array+[1]
  self._cumulative_prob=sum(count_array)
  self.symbol_count_to_probability_ranges()
 def symbol_count_to_probability_ranges(self):
  self._ranges[0]=0
  self._ranges[self.upper(EOF_CHAR)]=1
  self._cumulative_prob+=1
  for c in range(EOF_CHAR+1):
   self._ranges[c+1]+=self._ranges[c]
 def write_header(self):
  if self._outfile is None:
   raise ArithmeticCodeError('No output file opened for encoding.')
  previous=0
  for c in range(EOF_CHAR):
   if self._ranges[self.upper(c)]>previous:
    self._outfile.put_char(c)
    previous=(self._ranges[self.upper(c)]-previous)
    self._outfile.put_bits_ltom(previous,(PRECISION-2))
    previous=self._ranges[self.upper(c)]
  self._outfile.put_char(0)
  previous=0
  self._outfile.put_bits_ltom(previous,(PRECISION-2))
 def initialize_adaptive_probability_range_list(self):
  self._ranges=[i for i in range(self.upper(EOF_CHAR)+1)]
  self._cumulative_prob=EOF_CHAR+1
 def apply_symbol_range(self,symbol):
  range=self._upper-self._lower+1
  rescaled=self._ranges[self.upper(symbol)]*range
  rescaled/=self._cumulative_prob
  self._upper=self._lower+rescaled-1
  rescaled=self._ranges[self.lower(symbol)]*range
  rescaled/=self._cumulative_prob
  self._lower=self._lower+rescaled
  if not self._static_model:
   self._cumulative_prob+=1
   for i in range(self.upper(symbol),len(self._ranges)):
    self._ranges[i]+=1
   if self._cumulative_prob>=MAX_PROBABILITY:
    original=0
    for i in range(1,len(self._ranges)):
     delta=self._ranges[i]-original
     original=self._ranges[i]
     if delta<=2:
      self._ranges[i]=self._ranges[i-1]+1
     else:
      self._ranges[i]=self._ranges[i-1]+(delta/2)
    self._cumulative_prob=self._ranges[self.upper(EOF_CHAR)]
 def write_encoded_bits(self):
  if self._outfile is None:
   raise ArithmeticCodeError('No output file opened for encoding.')
  mask_bit_zero=self.mask_bit(0)
  mask_bit_one=self.mask_bit(1)
  while True:
   if(self._upper^~self._lower)&mask_bit_zero:
    self._outfile.put_bit((self._upper&mask_bit_zero)!=0)
    while self._underflow_bits>0:
     self._outfile.put_bit((self._upper&mask_bit_zero)==0)
     self._underflow_bits-=1
   elif(~self._upper&self._lower)&mask_bit_one:
    self._underflow_bits+=1
    self._lower&=~(mask_bit_zero|mask_bit_one)
    self._upper|=mask_bit_one
   else:
    return
   self._lower&=MSB_MASK
   self._lower<<=1
   self._upper&=MSB_MASK
   self._upper<<=1
   self._upper|=0x0001
 def write_remaining(self):
  if self._outfile is None:
   raise ArithmeticCodeError('No output file opened for encoding.')
  mask_bit_one=self.mask_bit(1)
  self._outfile.put_bit((self._lower&mask_bit_one)!=0)
  self._underflow_bits+=1
  for i in range(self._underflow_bits):
   self._outfile.put_bit((self._lower&mask_bit_one)==0)
 def decode_file(self,input_file_name,output_file_name):
  if(self._infile is not None)or(self._outfile is not None):
   raise ValueError('I/O operation on opened file.')
  self._infile=bitfile.BitFile()
  self._infile.open(input_file_name,'rb')
  if self._static_model:
   self.read_header()
  else:
   self.initialize_adaptive_probability_range_list()
  self.initialize_decoder()
  self._outfile=open(output_file_name,'wb')
  while True:
   unscaled=self.get_unscaled_code()
   c=self.get_symbol_from_probability(unscaled)
   if c==EOF_CHAR:
    break
   self._outfile.write(chr(c))
   self.apply_symbol_range(c)
   self.read_encoded_bits()
  self._outfile.close()
  self._infile.close()
 def read_header(self):
  if self._infile is None:
   raise ArithmeticCodeError('No input file opened for decoding.')
  self._cumulative_prob=0
  self._ranges=[0 for i in range(self.upper(EOF_CHAR)+1)]
  count=0
  while True:
   c=self._infile.get_char()
   count=self._infile.get_bits_ltom(PRECISION-2)
   if count==0:
    break
   elif self._ranges[self.upper(c)]!=0:
    raise ArithmeticCodeError('Duplicate entry for '+hex(ord(c))+' in header.')
   self._ranges[self.upper(c)]=count
   self._cumulative_prob+=count
  self.symbol_count_to_probability_ranges()
 def initialize_decoder(self):
  self._code=0
  for i in range(PRECISION):
   self._code<<=1
   try:
    next_bit=self._infile.get_bit()
   except EOFError:
    pass
   except:
    raise
   else:
    self._code|=next_bit
  self._lower=0
  self._upper=0xFFFF
 def get_unscaled_code(self):
  range=self._upper-self._lower+1
  unscaled=self._code-self._lower+1
  unscaled=unscaled*self._cumulative_prob-1
  unscaled/=range
  return unscaled
 def get_symbol_from_probability(self,probability):
  first=0
  last=self.upper(EOF_CHAR)
  middle=last/2
  while(last>=first):
   if probability<self._ranges[self.lower(middle)]:
    last=middle-1
    middle=first+((last-first)/2)
   elif probability>=self._ranges[self.upper(middle)]:
    first=middle+1
    middle=first+((last-first)/2)
   else:
    return middle
  raise ValueError('Probability not in range.')
 def read_encoded_bits(self):
  mask_bit_zero=self.mask_bit(0)
  mask_bit_one=self.mask_bit(1)
  while True:
   if(self._upper^~self._lower)&mask_bit_zero:
    pass
   elif(~self._upper&self._lower)&mask_bit_one:
    self._lower&=~(mask_bit_zero|mask_bit_one)
    self._upper|=mask_bit_one
    self._code^=mask_bit_one
   else:
    return
   self._lower&=MSB_MASK
   self._lower<<=1
   self._upper&=MSB_MASK
   self._upper<<=1
   self._upper|=1
   self._code&=MSB_MASK
   self._code<<=1
   try:
    next_bit=self._infile.get_bit()
   except EOFError:
    pass
   except:
    raise
   else:
    self._code|=next_bit
import os
import filecmp
import tempfile
import unittest
class EncodeDirTest(unittest.TestCase):
 def setUp(self):
  self.dir=os.listdir('.')
  makesuffix=tempfile._RandomNameSequence()
  self.encoded=tempfile.gettempprefix()+next(makesuffix)
  self.decoded=tempfile.gettempprefix()+next(makesuffix)
  while self.encoded in self.dir:
   self.encoded=tempfile.gettempprefix()+next(makesuffix)
  while self.decoded in self.dir:
   self.decoded=tempfile.gettempprefix()+next(makesuffix)
  self.ar=ArithmeticCode()
 def tearDown(self):
  del self.ar
  if os.path.isfile(self.encoded):
   os.remove(self.encoded)
  if os.path.isfile(self.decoded):
   os.remove(self.decoded)
 def test_static(self):
  print('\nTests Using Static Model:')
  for src in self.dir:
   if os.path.isfile(src):
    print('\tEncoding',src)
    self.ar.__init__(True)
    self.ar.encode_file(src,self.encoded)
    print('\tDecoding',src)
    self.ar.__init__(True)
    self.ar.decode_file(self.encoded,self.decoded)
    self.assertTrue(filecmp.cmp(src,self.decoded),'Failed to Verify {0}'.format(src))
    os.remove(self.encoded)
    os.remove(self.decoded)
 def test_adaptive(self):
  print('\nTests Using Adaptive Model:')
  for src in self.dir:
   if os.path.isfile(src):
    print('\tEncoding',src)
    self.ar.__init__(False)
    self.ar.encode_file(src,self.encoded)
    print('\tDecoding',src)
    self.ar.__init__(False)
    self.ar.decode_file(self.encoded,self.decoded)
    self.assertTrue(filecmp.cmp(src,self.decoded),'Failed to Verify {0}'.format(src))
    os.remove(self.encoded)
    os.remove(self.decoded)
if __name__=="__main__":
 unittest.main()
