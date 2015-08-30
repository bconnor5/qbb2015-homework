import numpy as np
import copy

class Chrmloc(object):
   
                                            # self represents instance of object itself;                                                   explicity
     
      def __init__(self, dicts=None, fname=None):
            
            # If dicts parameter provided, use to initialize
            if dicts is not None:
                  
                  arrays = dicts     
            else: #what exactly?
                  arrays = {}
           
            if fname is not None:
                  for line in open ( fname ):
                        fields = line.split()
                        Chrm_name = fields[0]
                        size = int ( fields[1] )
                        arrays[Chrm_name] = np.zeros( size, dtype = bool )                                                                #arrays[Chrm_name]?
            self.arrays = arrays
      
      def set_bits_from_file( self, fname ):
            
            for line in open( fname ):
                  fields = line.split()
                  Chrm_name = fields[0]
                  Strt_Pos = int (fields[1])
                  Stop_Pos = int (fields[2])
                  self.arrays[ Chrm_name ][ Strt_Pos : Stop_Pos ] = 1 
                  
      """nested self.() apends array"""
      
      def intersect( self, other ):
            
            rval = {}
            
            for Chrm_name in self.arrays:
                  rval[ Chrm_name ] = self.arrays[ Chrm_name ] & other.arrays[ Chrm_name ]
            return Chrmloc( dicts = rval) 
            
      def union( self, other ):
            rval = {}
            for Chrm_name in self.arrays:
                  rval[ Chrm_name ] = self.arrays[ Chrm_name] | other.arrays[ Chrm_name ]
            return Chrmloc( dicts = rval )
            
      def complement( self ):
            
            rval = {}
            
            for Chrm_name in self.arrays:
                  rval[ Chrm_name ] = ~ self.arrays[ Chrm_name ]
            return Chrmloc( dicts = rval )
            
      def copy( self ):
            
            return Chrmloc(dicts = copy.deepcopy(self.arrays))
            
      """add method to return (tuple list) of chromosome, start stop location"""
      
      def bed( self ):
            
            data = []
            for Chrm_name in self.arrays:
                  row = self.arrays[Chrm_name]
                  for i, x in enumerate(row):
                        
                        if x == 1 and row[i-1] == 0:   #edit line 72-75 to compensate for edge position loss
                             Strt_Pos = i
                        if x == 0 and row[i-1] == 1:
                              Stop_Pos = i
                              data.append((Chrm_name, Strt_Pos, Stop_Pos))
            return data
            
                  